#!/usr/bin/env python3
"""
spool_dump.py — Read a SPOOLMAST flat binary file and emit each active record
as a JSON array to stdout, newest-first (matching the Spool Queue Viewer order).

Records with status "6" (purged) are always silently skipped.

Usage:
    python3 spool_dump.py <spool_dir> [status_filter] [filename_filter]

    spool_dir       - directory containing the SPOOLMAST file
    status_filter   - optional; restrict output to one status code:
                      1=ON QUEUE  2=PRINTING  3=PRINTED
                      4=ABORTED   5=KEEP      ALL (default)
    filename_filter - optional; restrict output to records whose filename
                      contains this string (case-insensitive)

SPOOLMAST record layout (128 bytes per record, offsets 1-based):
    Record 0 (header): bytes 1-4 = next free record index (big-endian uint32)
    Records 1..N:
        [  1-  4] entry number   (big-endian uint32)
        [  5- 16] filename       (12 chars)
        [ 17- 46] description    (30 chars)
        [ 47- 56] stationery     (10 chars)
        [     57] status code    (1 char: 1=ON QUEUE 2=PRINTING 3=PRINTED
                                          4=ABORTED  5=KEEP     6=purged/skip)
        [     58] delete flag    (1 char)
        [ 59- 62] date req       (4-byte packed BCD CCYYMMDD)
        [ 63- 66] date actual    (4-byte packed BCD CCYYMMDD; 0 = not yet printed)
        [ 67- 69] time queued    (3-byte packed BCD HHMMSS)
        [ 70- 72] time printed   (3-byte packed BCD HHMMSS; 0 = not yet printed)
        [ 73- 76] user           (4 chars — who requested the job)
        [ 77- 80] operator       (4 chars — who physically printed; may differ from user)
        [     81] printer        (1 char ASCII digit — printer/device number)
        [ 82- 83] company        (2 chars)
        [     84] system code    (1 char: A=Accounts S=Stock P=Sales
                                          C=Contract <space>=Global)
        [     85] copies         (binary integer)
        [     86] reserved flag  (1 byte, always 0)
        [ 87-116] reserved text  (30 chars, always blank)
        [117-128] reserved       (12 bytes, always 0)
"""

import json
import os
import struct
import sys

REC_SIZE = 128

STATUS_LABELS = {
    '1': 'ON QUEUE',
    '2': 'PRINTING',
    '3': 'PRINTED',
    '4': 'ABORTED',
    '5': 'KEEP',
}

SYSTEM_LABELS = {
    'A': 'Accounts',
    'S': 'Stock',
    'P': 'Sales',
    'C': 'Contract',
    ' ': 'Global',
}


def bcd_date(raw: bytes) -> str:
    """Convert 4-byte packed BCD CCYYMMDD to DD/MM/CCYY string, or '' if zero."""
    h = raw.hex()  # e.g. b'\x19\x98\x10\x05' -> '19981005'
    if h == '00000000':
        return ''
    return f'{h[6:8]}/{h[4:6]}/{h[0:4]}'


def bcd_time(raw: bytes) -> str:
    """Convert 3-byte packed BCD HHMMSS to HH:MM:SS string, or '' if zero."""
    h = raw.hex()  # e.g. b'\x08\x46\x12' -> '084612'
    if h == '000000':
        return ''
    return f'{h[0:2]}:{h[2:4]}:{h[4:6]}'


def parse_record(i: int, rec: bytes) -> dict:
    entry      = struct.unpack('>I', rec[0:4])[0]
    filename   = rec[4:16].decode('latin1').rstrip()
    desc       = rec[16:46].decode('latin1').rstrip()
    stationery = rec[46:56].decode('latin1').rstrip()
    stat_byte  = chr(rec[56])
    date_req   = bcd_date(rec[58:62])
    date_act   = bcd_date(rec[62:66])
    time_q     = bcd_time(rec[66:69])
    time_p     = bcd_time(rec[69:72])
    user       = rec[72:76].decode('latin1').rstrip()
    operator   = rec[76:80].decode('latin1').rstrip()
    printer    = chr(rec[80])
    company    = rec[81:83].decode('latin1').rstrip()
    sys_byte   = chr(rec[83])
    copies     = rec[84]

    return {
        'rowid':       i,
        'entry':       entry,
        'filename':    filename,
        'description': desc,
        'stationery':  stationery,
        'status':      STATUS_LABELS.get(stat_byte, 'UNKNOWN'),
        'statusCode':  stat_byte,
        'dateReq':     date_req,
        'dateActual':  date_act,
        'timeQueued':  time_q,
        'timePrinted': time_p,
        'user':        user,
        'operator':    operator,
        'printer':     printer,
        'company':     company,
        'system':      SYSTEM_LABELS.get(sys_byte, sys_byte.strip()),
        'copies':      copies,
    }


def main():
    if len(sys.argv) < 2:
        print('{"error":"Usage: python3 spool_dump.py <spool_dir> [status_filter]"}')
        sys.exit(1)

    spool_dir = sys.argv[1].rstrip('/')
    status_filter   = sys.argv[2].upper() if len(sys.argv) > 2 else 'ALL'
    filename_filter = sys.argv[3].upper() if len(sys.argv) > 3 else ''
    path = os.path.join(spool_dir, 'SPOOLMAST')

    try:
        with open(path, 'rb') as f:
            data = f.read()
    except OSError as e:
        print(json.dumps({'error': f"Cannot open SPOOLMAST in '{spool_dir}': {e}"}))
        sys.exit(1)

    next_free = struct.unpack('>I', data[0:4])[0]
    if next_free <= 1:
        print('[]')
        return

    records = []
    for i in range(next_free - 1, 0, -1):   # newest-first
        rec = data[i * REC_SIZE : (i + 1) * REC_SIZE]
        stat_byte = chr(rec[56])
        if stat_byte == '6':
            continue
        if status_filter != 'ALL' and stat_byte != status_filter:
            continue
        if filename_filter and filename_filter not in rec[4:16].decode('latin1').upper():
            continue
        records.append(parse_record(i, rec))

    print(json.dumps(records, indent=2))


if __name__ == '__main__':
    main()
