# Related Products

> The tools and components that work alongside the KCML language engine: the client application, built-in database, mail client, and distributed printing system.

## KCML Client (Kclient)

Kclient is a freely distributable Windows application (Windows 9x / NT) that acts as the presentation layer for KCML server programs. A KCML program running on the server drives the client, which renders:

- **GUI forms** designed in the Workbench forms editor.
- **Text windows** for applications that use terminal-style output.

Kclient is the standard deployment mechanism for client/server KCML applications. It communicates with the KCML server over TCP/IP.

## Kerridge Database (KISAM)

KCML includes a built-in relational database engine using fast **B-tree indexing**. It is accessed in two ways:

| Access method | Description |
|---------------|-------------|
| **SQL** | Standard SQL queries against KISAM tables. |
| **ISAM (rowset)** | Direct sequential and keyed access to table rows — fast for high-volume transaction processing. |

KISAM is the recommended storage mechanism for all structured data in KCML applications.

## Kerridge Mail (KMail)

KMail is a Windows-based mail client for PCs connected to a Unix host over TCP/IP. It uses **industry-standard mail protocols and formats** to ensure interoperability with other mail systems.

Architecture:
- The Unix host acts as a mail router and message store.
- KMail connects to the host to send and retrieve messages.
- Because standard protocols are used, messages can be exchanged freely with non-KMail users.

## Kprint

Kprint is a distributed printing solution designed for high-quality laser printer output across wide area networks. It eliminates the need for expensive pre-printed stationery by combining plain ASCII text with rich document templates on the client side.

How it works:

1. The KCML server sends plain ASCII text to a **Kprint server** on a Windows NT or 95 PC using the standard **LPD protocol** (Internet standard).
2. The Kprint server merges the text with a stored **document definition** to produce a rich document using bitmaps, multiple fonts, and line drawing.
3. The finished document is sent to the local printer.

Additional Kprint features:

- **Fax and email output** support.
- Standard report printing.
- Automatic distribution and caching of document definitions to remote Kprint servers — no manual installation needed at each site.
- A **WYSIWYG editor** for creating and modifying form templates.

The result: print jobs from a central Unix server produce polished, form-like output on printers anywhere on the WAN, with no changes required to the KCML application.

## Notes

- Kclient is the preferred client for all new GUI development; the older Kerridge Terminal Emulator is still available for legacy serial/TCP text connections.
- KISAM is covered in depth in the File I/O chapters of this manual.
- Kprint requires no code changes on the KCML server side — it is transparent to the application.
