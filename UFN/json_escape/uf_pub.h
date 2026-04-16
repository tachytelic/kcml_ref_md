/* $Id: uf_pub.h,v 1.56.4.2 2014/03/10 17:29:44 kccrjc Exp $ */
/*
** uf_pub.h - User Function Public Header File
**
** used with UNIX and NT
**
*/

#ifndef __UF_PUB_H
#define __UF_PUB_H

#ifdef __cplusplus
extern "C" {
#endif

/* define -DUNIX for Unix compilations */
#ifdef UNIX
#if defined(__GNUC__) && !defined(SUN)
/* If code is compiled with -fvisibility=hidden we need to make the entry point visible */
#define UFN_EXPORT	 __attribute__ ((visibility("default")))
#else
#define UFN_EXPORT
#endif
#define UFN_API
#else
/* this should work with both MSC and Watcom 11 */
#define UFN_API		__stdcall
#define UFN_EXPORT	__declspec(dllexport) __stdcall
#ifndef WINAPI
#error You forgot <windows.h>
#endif
#endif


/* 32-bit case */
#if defined(CHAR_IS_UNSIGNED) || defined(_CHAR_UNSIGNED)
typedef char		KCMLUCHAR;	/* unsigned character		*/
#else
typedef unsigned char	KCMLUCHAR;	/* unsigned character		*/
#endif
typedef unsigned int	KCMLUINT;	/* unsigned 4 byte int		*/
typedef int		KCMLINT;	/* signed 4 byte int		*/
typedef double		KCMLDOUBLE;	/* Native double format		*/
typedef KCMLUCHAR *	KCMLPCHAR;	/* Pointer to character		*/
typedef void *		PROCADDR;	/* Pointer to function		*/

#ifndef _BASIK_H
typedef int		Sy_lindex;
#endif


#ifndef UFN_MAX_PARAMS
// values for UFN_Spec->Param[]
// Values are fixed for backward compatibility with existing libraries
// If you add to this list, update the text descriptions uf_text[] in ct_pure.c
typedef enum {
	UFN_FD			= 0x01,		// file descriptor
	UFN_SYMBOL		= 0x02,		// symbol
	UFN_KSTR		= 0x03,		// string
	UFN_INT			= 0x04,		// int
	UFN_DOUBLE		= 0x05,		// double
	UFN_CSTR		= 0x06,		// 'C' string (null terminated)
	UFN_PSTR		= 0x07,		// Pascal string 1 byte length
	UFN_SYMPTR		= 0x08,		// symbol pointer
	UFN_FSTR		= 0x09,		// Far pointer to string
	UFN_SYMBOLANY		= 0x0A,		// numeric or string sym()
	UFN_INTORKSTR		= 0x0B,		// numeric or string
	UFN_THANDLE		= 0x0C,		// table handle
	UFN_CHANDLE		= 0x0D,		// connection handle
	UFN_SYMREC		= 0x0E,		// SYM of a record
	UFN_BOOL		= 0x0F,		// Boolean
	UFN_ENUM		= 0x10,		// Enumeration using KCML built in constants
	UFN_KDB_ERROR_ENUM	= 0x11,		// KDB status code
	UFN_XHANDLE		= 0x12,		// XML file handle

	UFN_ARG_TYPE_LAST,	// Max value marker, must be the last entry

	// Flags
	UFN_FLAG_OPT		= 0x20,		// optional parameter
	UFN_FLAG_ARRAY		= 0x40,		// array of ...
	UFN_FLAG_RCVR		= 0x80,		// parameter is a receiver
} UfnArgType;

#define OPTPAR(x)	(UfnArgType)((x) | UFN_FLAG_OPT)
#define ARRAY(x)	(UfnArgType)((x) | UFN_FLAG_ARRAY)
#define RCVR(x)		(UfnArgType)((x) | UFN_FLAG_RCVR)

// max number of parameters
#define UFN_MAX_PARAMS	12
#endif

// max size of function name supported
#define UFN_NAMELEN	32

// max number of calls in a table (limited by using a BYTE for ordinal counts)
# define UFN_MAX_CALLS	255

#ifndef UNIX
/* force 4 byte alignment as this is what KCML uses of 5.02 */
#include <pshpack4.h>
#endif

// Details for String value or receiver
// This should be congruent with KI_BUF_SPEC in kdb
typedef	struct	UFN_Pstr {
	KCMLPCHAR	sptr;		/* pointer to slen bytes	*/
	KCMLUINT	slen;		/* length of string		*/
	KCMLUINT	attr;		/* attributes (used by SYM)	*/
} UFN_Pstr;

/* Details for Numeric array value or receiver */
typedef	struct	UFN_Pna {
	KCMLDOUBLE	*aptr;		/* pointer to numeric values	*/
	KCMLUINT	dim;		/* dimension, 0 is illegal	*/
} UFN_Pna;


/* Details for String array value or receiver */
typedef	struct	UFN_Psa {
	KCMLPCHAR	aptr;		/* pointer to characters	*/
	KCMLUINT	dim;		/* dimension, 0 is illegal	*/
	KCMLUINT	slen;		/* length of each element	*/
} UFN_Psa;

/*
** Array descriptor, first 2 elements are congruent with Sy_arrayinfo
** type as it might be casted to one of those.
*/
typedef struct {
	struct Sy_array		*array;
	int			type;		// Sy_type enum
	struct Sy_entry		*pent;		// KCML6 only: Original symbol table entry
	Sy_lindex		sym;		// KCML6 and KCML7
} KCMLARRAYINFO;

/* Details for symbol and sign - used by KI_DIR */
typedef	struct	UFN_Sym {
	KCMLARRAYINFO	arrayinfo;	// info about array (not same layout as Sy_arrayinfo)
	KCMLUINT	bRedim;		/* redim?			*/
} UFN_Sym;

// UFN_SYMREC, SYM(rec$)
// This should be congruent with KI_ROW_SPEC in kdb
typedef struct UFN_rec {
	char		*ptr;		// ptr to buffer or NULL of none
	int		len;		// defined length
	const void	*view;		// possible view column map
} UFN_rec;

// union of possible parameter types
typedef	union UFN_Value {
	KCMLDOUBLE	nval;		/* numeric value		*/
	KCMLINT		ival;		/* integer value		*/
	UFN_Pstr	s;		/* string			*/
	UFN_Pna		na;		/* numeric array		*/
	UFN_Psa		sa;		/* string array			*/
	KCMLINT		fd;		/* file descriptor		*/
	UFN_Sym		arr;		/* symbol			*/
	UFN_rec		rec;		// Used for UFN_SYMREC
} UFN_Value;

// parameter block passed to a UFN function by CALL
typedef struct UFN_args {
	int		err;			// return code (reserved for UFN_KE_FATAL exits)
	int		dummy;			// avoid any alignment issues
	UFN_Value	u[UFN_MAX_PARAMS];	// the arguments
} UFN_args;

#ifndef UNIX
/* restore original structure packing */
#include <poppack.h>
#endif

// return codes and their type, these must align with the errtab[] table in uf_code.c
typedef enum {
	UFN_SUCCESS	= 0,		// function succeeded
	// these calls map to berrors in errtab[]
	UFN_BADARGS	= 1,		// bad arguments to function
	UFN_ERROR	= 2,		// function failed recoverably
	UFN_FATAL	= 3,		// function failed unrecoverably
	UFN_KE_FATAL	= 4,		// DB call failed with app programming bug, throw error
	// these calls are specially handled
	UFN_RETRY_CALL	= 5,		// Re-issue CALL after DB failover
	UFN_RETRY_TX	= 6,		// WHILE TRANS to be restarted after failover or deadlock
	UFN_PANIC	= 7,		// DB call failed because server killed, panic and exit
} UFN_RET;

#define UFN_ARGS	UFN_args *pb
#define UFN_ARG		pb

/*
** Type for entries in UFN Lookup Table
** Set the nCall member to be the ordinal in the array, e.g. 1 for first, 2 for second, ...
*/
typedef	struct {
	const char	*name;					// name CALLed in KCML
	UFN_RET		(UFN_API *function)(UFN_ARGS);		// the C function to call
	UfnArgType	Param[UFN_MAX_PARAMS+1];		// type info for the args
} UFN_Spec;

typedef const UFN_Spec *	PUFN_Spec;

#define NVAL(x)		(pb->u[(x)].nval)
#define IVAL(x)		(pb->u[(x)].ival)
#define NINT(x)		(IVAL(x))
#define SVAL(x)		(pb->u[(x)].s.sptr)
#define SLEN(x)		(pb->u[(x)].s.slen)
#define SATTR(x)	(pb->u[(x)].s.attr)
#define ARPTR(x)	(pb->u[(x)].arr.arrayinfo.array)
#define ARPENT(x)	(pb->u[(x)].arr.arrayinfo.pent)
#define ARSYM(x)	(pb->u[(x)].arr.arrayinfo.sym)
#define ARREDIM(x)	(pb->u[(x)].arr.bRedim)
#define ARINFO(x)	((struct Sy_arrayinfo *)(&pb->u[(x)].arr.arrayinfo))
// see uf_db.c for some more macros using UFN_ARG


#define SATTR_STRING	0
#define SATTR_NUMBER	1

/* malloc, realloc, free pointers
**
** The idea in KCML3 was to pass these to the external routines
** so that they did not call the C runtime versions directly and
** interfere with the KCML memory managers use of sbrk().  In KCML4
** and later this is no longer a problem so this mechanism is not
** needed.  You can call them directly if needed.
*/
typedef struct {
	void	*(*malloc)(int size);		/* malloc		*/
	void	*(*realloc)(void *p, int size);	/* realloc		*/
	void	(*free)(void *p);		/* free			*/
} UFN_Subs;

/* only valid in ufn_ext() and below ( use of->) */
#define UFN_MALLOC(x)		(KcmlSubs->malloc(x))
#define UFN_REALLOC(x,y)	(KcmlSubs->realloc(x),(y))
#define UFN_FREE(x)		(KcmlSubs->free(x))

#if !defined(__cplusplus) || (AS_CPLUSPLUS)

/* type for entry point */
typedef PUFN_Spec (UFN_API *UFN_EXT_FUNC)(const UFN_Subs *ptr);
#endif

/* prototype for entry point */
extern PUFN_Spec UFN_EXPORT uf_ext(const UFN_Subs *p);

#ifdef __cplusplus
} // extern "C"
#endif

// !__UF_PUB_H
#endif
