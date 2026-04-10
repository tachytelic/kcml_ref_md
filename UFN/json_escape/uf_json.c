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
**   raw$ = "100MM X 33M (4" X 36yds)"
**   CALL JSON_ESCAPE raw$ TO escaped$
**   PRINT $PRINTF("  ""desc"": ""%s""", escaped$)
**
** Build:
**   make -f uf_json.mak
**
** Load:
**   kcml -x /path/to/uf_json.so -p pik_to_json.kcml <args>
*/

#include <stdio.h>
#include <string.h>
#include "uf_pub.h"

/* function prototype */
static UFN_RET UFN_API json_escape(UFN_ARGS);

/*
** UFN table - MUST be in sorted (ASCII) order by name
*/
static UFN_Spec UFN_Table[] = {
    { "JSON_ESCAPE", 0, json_escape, { CSTR, RCVR(CSTR), 0 } },
    { "", 0, 0, { 0 } }, /* end marker */
};

/*
** Library entry point - called by KCML on first use of any function
** in this library.
*/
UFN_Spec * UFN_API uf_ext(UFN_Subs *p)
{
    return UFN_Table;
}

/*
** json_escape
**
** Escapes a string for safe inclusion as a JSON string value.
** The caller is responsible for emitting the surrounding double-quotes.
**
** Parameter 0 (CSTR)       - input string
** Parameter 1 (RCVR(CSTR)) - output buffer (must be at least 2x input size
**                            in the worst case where every char is a quote)
**
** Returns UFN_BADARGS if the output buffer is too small.
*/
static UFN_RET UFN_API json_escape(UFN_ARGS)
{
    const char *in      = (const char *)SVAL(0);
    char       *out     = (char *)SVAL(1);
    unsigned    out_cap = SLEN(1);    /* declared size of output buffer */
    unsigned    o       = 0;
    char        c;

    while ((c = *in++) != '\0') {
        switch (c) {
            case '"':
                if (o + 2 >= out_cap) return UFN_BADARGS;
                out[o++] = '\\';
                out[o++] = '"';
                break;
            case '\\':
                if (o + 2 >= out_cap) return UFN_BADARGS;
                out[o++] = '\\';
                out[o++] = '\\';
                break;
            case '\n':
                if (o + 2 >= out_cap) return UFN_BADARGS;
                out[o++] = '\\';
                out[o++] = 'n';
                break;
            case '\r':
                if (o + 2 >= out_cap) return UFN_BADARGS;
                out[o++] = '\\';
                out[o++] = 'r';
                break;
            case '\t':
                if (o + 2 >= out_cap) return UFN_BADARGS;
                out[o++] = '\\';
                out[o++] = 't';
                break;
            default:
                if ((unsigned char)c < 0x20) {
                    /* other control characters: emit as \u00XX */
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
