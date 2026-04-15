/*
** uf_json_parse.c - KCML User Functions for JSON parsing via cJSON
**
** Provides a handle-based JSON parser for KCML 6.9.
** Parse once, navigate by dotted path, free when done.
**
** Functions (KCML CALL syntax):
**
**   CALL JSON_PARSE  json_str$          TO handle
**   CALL JSON_GET_STR  handle, "path"   TO value$
**   CALL JSON_GET_NUM  handle, "path"   TO nval
**   CALL JSON_ARRAY_LEN handle, "path"  TO count
**   CALL JSON_FREE   handle
**
** Path syntax:
**   "key"              - top-level key
**   "key.subkey"       - nested object
**   "key[0]"           - array element
**   "key[0].subkey"    - array element then nested key
**   ""                 - root (useful for JSON_ARRAY_LEN on a top-level array)
**
** Example KCML usage:
**   DIM h, count, price, name$64
**   CALL JSON_PARSE resp$ TO h
**   IF h == 0 THEN PRINT "parse failed"
**   IF h == 0 THEN $END
**   CALL JSON_GET_STR h, "customer.name" TO name$
**   CALL JSON_GET_NUM h, "order.total"   TO price
**   CALL JSON_ARRAY_LEN h, "order.lines" TO count
**   PRINT RTRIM(name$); " owes "; price; " with "; count; " lines"
**   CALL JSON_FREE h
**
** Build:
**   make -f uf_json_parse.mak
**
** Load:
**   kcml -x ./uf_json_parse.so -p myscript.kcml
**
** Compiled against: cJSON 1.7.17 (bundled), KCML 06.00.xx (32-bit)
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cJSON.h"
#include "uf_pub.h"

/* ------------------------------------------------------------------ */
/* Handle table                                                          */
/* ------------------------------------------------------------------ */

#define MAX_HANDLES 64

static cJSON *g_handles[MAX_HANDLES + 1];   /* 1-based; 0 = invalid  */
static int    g_initialised = 0;

static void init_handles(void)
{
    if (!g_initialised) {
        memset(g_handles, 0, sizeof(g_handles));
        g_initialised = 1;
    }
}

static int alloc_handle(cJSON *tree)
{
    int i;
    init_handles();
    for (i = 1; i <= MAX_HANDLES; i++) {
        if (g_handles[i] == NULL) {
            g_handles[i] = tree;
            return i;
        }
    }
    return 0;   /* no free slot */
}

static cJSON *get_handle(int h)
{
    init_handles();
    if (h < 1 || h > MAX_HANDLES) return NULL;
    return g_handles[h];
}

static void free_handle(int h)
{
    if (h < 1 || h > MAX_HANDLES) return;
    if (g_handles[h]) {
        cJSON_Delete(g_handles[h]);
        g_handles[h] = NULL;
    }
}

/* ------------------------------------------------------------------ */
/* Path navigation                                                       */
/* Navigate a dotted path like "order.lines[0].qty" through a cJSON    */
/* tree.  Returns NULL if the path does not resolve.                    */
/* ------------------------------------------------------------------ */

static cJSON *navigate(cJSON *node, const char *path)
{
    char buf[256];
    char *tok;

    if (!node) return NULL;
    if (!path || *path == '\0') return node;

    strncpy(buf, path, sizeof(buf) - 1);
    buf[sizeof(buf) - 1] = '\0';

    tok = buf;
    while (tok && *tok && node) {
        char *dot = strchr(tok, '.');
        char *seg;
        char segbuf[128];
        char *bracket;
        int  idx;

        if (dot) {
            size_t len = (size_t)(dot - tok);
            if (len >= sizeof(segbuf)) len = sizeof(segbuf) - 1;
            strncpy(segbuf, tok, len);
            segbuf[len] = '\0';
            seg = segbuf;
            tok = dot + 1;
        } else {
            seg = tok;
            tok = NULL;
        }

        /* check for array index suffix: key[N] */
        bracket = strchr(seg, '[');
        if (bracket) {
            *bracket = '\0';
            idx = atoi(bracket + 1);
            if (*seg != '\0')
                node = cJSON_GetObjectItemCaseSensitive(node, seg);
            if (node)
                node = cJSON_GetArrayItem(node, idx);
        } else {
            node = cJSON_GetObjectItemCaseSensitive(node, seg);
        }
    }

    return node;
}

/* ------------------------------------------------------------------ */
/* UFN implementations                                                   */
/* ------------------------------------------------------------------ */

/*
** JSON_PARSE  json_str$  TO  handle
**   param 0: UFN_CSTR    - JSON text (input, null-terminated)
**   param 1: RCVR(UFN_INT) - handle (output); 0 on parse error
*/
static UFN_RET UFN_API json_parse(UFN_ARGS)
{
    const char *text = (const char *)SVAL(0);
    cJSON      *tree;
    int         h;

    tree = cJSON_Parse(text);
    if (!tree) {
        IVAL(1) = 0;
        return UFN_SUCCESS;
    }

    h = alloc_handle(tree);
    if (h == 0) {
        cJSON_Delete(tree);
        IVAL(1) = 0;
        return UFN_ERROR;
    }

    IVAL(1) = h;
    return UFN_SUCCESS;
}

/*
** JSON_GET_STR  handle, "path"  TO  value$
**   param 0: UFN_INT  - handle
**   param 1: UFN_CSTR - dotted path
**   param 2: RCVR(UFN_CSTR) - result (empty string if not found)
*/
static UFN_RET UFN_API json_get_str(UFN_ARGS)
{
    int         h    = IVAL(0);
    const char *path = (const char *)SVAL(1);
    char       *out  = (char *)SVAL(2);
    unsigned    cap  = SLEN(2);
    cJSON      *node;
    const char *val;
    size_t      vlen;

    out[0] = '\0';

    node = navigate(get_handle(h), path);
    if (!node || !cJSON_IsString(node)) return UFN_SUCCESS;

    val  = node->valuestring;
    vlen = strlen(val);
    if (vlen >= cap) vlen = cap - 1;
    memcpy(out, val, vlen);
    out[vlen] = '\0';

    return UFN_SUCCESS;
}

/*
** JSON_GET_NUM  handle, "path"  TO  nval
**   param 0: UFN_INT    - handle
**   param 1: UFN_CSTR   - dotted path
**   param 2: RCVR(UFN_DOUBLE) - result (0 if not found)
*/
static UFN_RET UFN_API json_get_num(UFN_ARGS)
{
    int         h    = IVAL(0);
    const char *path = (const char *)SVAL(1);
    cJSON      *node;

    NVAL(2) = 0.0;

    node = navigate(get_handle(h), path);
    if (!node) return UFN_SUCCESS;

    if (cJSON_IsNumber(node))
        NVAL(2) = node->valuedouble;
    else if (cJSON_IsBool(node))
        NVAL(2) = cJSON_IsTrue(node) ? 1.0 : 0.0;

    return UFN_SUCCESS;
}

/*
** JSON_ARRAY_LEN  handle, "path"  TO  count
**   param 0: UFN_INT  - handle
**   param 1: UFN_CSTR - dotted path (empty = root)
**   param 2: RCVR(UFN_INT) - array element count; 0 if not array
*/
static UFN_RET UFN_API json_array_len(UFN_ARGS)
{
    int         h    = IVAL(0);
    const char *path = (const char *)SVAL(1);
    cJSON      *node;

    IVAL(2) = 0;

    node = navigate(get_handle(h), path);
    if (node && cJSON_IsArray(node))
        IVAL(2) = cJSON_GetArraySize(node);

    return UFN_SUCCESS;
}

/*
** JSON_FREE  handle
**   param 0: UFN_INT - handle to release
*/
static UFN_RET UFN_API json_free(UFN_ARGS)
{
    free_handle(IVAL(0));
    return UFN_SUCCESS;
}

/* ------------------------------------------------------------------ */
/* Function table - MUST be in ASCII-sorted order by name              */
/* ------------------------------------------------------------------ */

static const UFN_Spec UFN_Table[] = {
    { "JSON_ARRAY_LEN", json_array_len, { UFN_INT, UFN_CSTR, RCVR(UFN_INT),    0 } },
    { "JSON_FREE",      json_free,      { UFN_INT,                              0 } },
    { "JSON_GET_NUM",   json_get_num,   { UFN_INT, UFN_CSTR, RCVR(UFN_DOUBLE),  0 } },
    { "JSON_GET_STR",   json_get_str,   { UFN_INT, UFN_CSTR, RCVR(UFN_CSTR),    0 } },
    { "JSON_PARSE",     json_parse,     { UFN_CSTR, RCVR(UFN_INT),              0 } },
    { 0 }   /* end marker */
};

/* ------------------------------------------------------------------ */
/* Library entry point                                                   */
/* ------------------------------------------------------------------ */

PUFN_Spec UFN_EXPORT uf_ext(const UFN_Subs *p)
{
    (void)p;
    return UFN_Table;
}
