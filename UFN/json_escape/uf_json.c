/*
** uf_json.c - KCML User Functions for JSON string handling
**
** Provides JSON_ESCAPE: takes a string, returns a version safe for
** embedding inside a JSON double-quoted string value.
**
** Characters escaped:
**   "  ->  \"
**   \  ->  \\
**   control chars (< 0x20) -> \uXXXX  (or named: \n \r \t)
**
** KCML usage:
**   DIM raw$256, escaped$512
**   CALL JSON_ESCAPE raw$ TO escaped$
**   PRINT $PRINTF("  ""desc"": ""%s""", escaped$)
**
** Build:
**   make -f uf_json.mak
**
** Load:
**   kcml -x /path/to/uf_json.so -p myscript.kcml
**
** Compiled against: KCML 06.00.xx uf_pub.h (2014, new API), 32-bit
*/

#include <stdio.h>
#include <string.h>
#include "uf_pub.h"

static UFN_RET UFN_API json_escape(UFN_ARGS);

static const UFN_Spec UFN_Table[] = {
    { "JSON_ESCAPE", json_escape, { UFN_CSTR, RCVR(UFN_CSTR), 0 } },
    { 0 }   /* end marker */
};

PUFN_Spec UFN_EXPORT uf_ext(const UFN_Subs *p)
{
    (void)p;
    return UFN_Table;
}

/*
** json_escape
**
** Parameter 0 (UFN_CSTR)       - input string
** Parameter 1 (RCVR(UFN_CSTR)) - output buffer (at least 2x input size)
**
** Returns UFN_BADARGS if the output buffer is too small.
*/
static UFN_RET UFN_API json_escape(UFN_ARGS)
{
    const char *in      = (const char *)SVAL(0);
    char       *out     = (char *)SVAL(1);
    unsigned    out_cap = SLEN(1);
    unsigned    o       = 0;
    char        c;

    while ((c = *in++) != '\0') {
        switch (c) {
            case '"':
                if (o + 2 >= out_cap) return UFN_BADARGS;
                out[o++] = '\\'; out[o++] = '"';
                break;
            case '\\':
                if (o + 2 >= out_cap) return UFN_BADARGS;
                out[o++] = '\\'; out[o++] = '\\';
                break;
            case '\n':
                if (o + 2 >= out_cap) return UFN_BADARGS;
                out[o++] = '\\'; out[o++] = 'n';
                break;
            case '\r':
                if (o + 2 >= out_cap) return UFN_BADARGS;
                out[o++] = '\\'; out[o++] = 'r';
                break;
            case '\t':
                if (o + 2 >= out_cap) return UFN_BADARGS;
                out[o++] = '\\'; out[o++] = 't';
                break;
            default:
                if ((unsigned char)c < 0x20) {
                    if (o + 6 >= out_cap) return UFN_BADARGS;
                    sprintf(out + o, "\\u%04x", (unsigned char)c);
                    o += 6;
                } else {
                    if (o + 1 >= out_cap) return UFN_BADARGS;
                    out[o++] = c;
                }
                break;
        }
    }
    out[o] = '\0';
    return UFN_SUCCESS;
}
