/* $Id: uf_pub.h,v 1.24.2.2 2005/03/23 12:39:12 dist Exp $ */
/*
** uf_pub.h - User Function Public Header File 
**
** used with UNIX and NT
**
*/

/* Some UNIX compilers do not support the const keyword. In this case
** they should pre-define CONST to be nothing.
*/
#ifndef CONST
#define CONST const
#endif

/* define -DUNIX for Unix compilations */
#ifdef UNIX
#define UFN_API	
#else
/* this should work with both MSC and Watcom 11 */
#define UFN_API	WINAPI
#ifndef WINAPI
#error You forgot <windows.h>
#endif
#endif


/* 32-bit case */
typedef unsigned char	KCMLUCHAR;	/* unsigned character		*/
typedef unsigned int	KCMLUINT;	/* unsigned 4 byte int 		*/
typedef int		KCMLINT;	/* signed 4 byte int 		*/
typedef double		KCMLDOUBLE;	/* Native double format 	*/
typedef KCMLUCHAR *	KCMLPCHAR;	/* Pointer to character		*/
typedef void *		PROCADDR;	/* Pointer to function 		*/


#ifndef MAXPARAMS
/* values for UFN_Spec -> Param[] */
#define RCVR(x)		((x) | 0x80)	/* parameter is a receiver	*/
#define ARRAY(x)	((x) | 0x40)	/* array of ...			*/
#define OPTPAR(x)	((x) | 0x20)	/* optional parameter		*/

#define INTORKSTR	0x0B		/* numeric or string 		*/
#define SYMBOLANY	0x0A		/* numeric or string sym()	*/
#define FSTR		0x09		/* Far pointer to string        */
#define SYMPTR		0x08		/* symbol pointer		*/
#define PSTR		0x07		/* Pascal string 1 byte length	*/
#define CSTR		0x06		/* 'C' string (null terminated)	*/
#define DOUBLE		0x05		/* double			*/
#define INT		0x04		/* int				*/
#define KSTR		0x03		/* string			*/
#define SYMBOL		0x02		/* symbol			*/
#define FD		0x01		/* file descriptor		*/
#define UFN_MAX_TYPES	11		/* elements in uf_text[]	*/

/* max number of parameters	*/
#define MAXPARAMS	12		
#endif

/* maximum name length */
#define UFN_NAMELEN	23

#ifndef UNIX
/* force 4 byte alignment as this is what KCML uses of 5.02 */
#include <pshpack4.h>
#endif

/* Details for String value or receiver */
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

/* Details for symbol and sign - used by KI_DIR */
typedef	struct	UFN_Sym {
	void		*sym_ptr;	/* KCML symbol pointer		*/
	KCMLUINT	bRedim;		/* redim?			*/
} UFN_Sym;


/* union of possible parameter types */
typedef	union UFN_Value {
	KCMLDOUBLE	nval;		/* numeric value		*/
	KCMLINT		ival;		/* integer value		*/
	UFN_Pstr	s;		/* string			*/
	UFN_Pna		na;		/* numeric array		*/
	UFN_Psa		sa;		/* string array			*/
	KCMLINT		fd;		/* file descriptor		*/
	UFN_Sym		sym;		/* symbol			*/
} UFN_Value;

#ifndef UNIX
/* restore original structure packing */
#include <poppack.h>
#endif

/* return codes and their type */
typedef enum {
	UFN_SUCCESS	=0,		/* function succeeded		*/
	UFN_BADARGS	=1,		/* bad arguments to function	*/
	UFN_ERROR	=2,		/* function failed recoverably	*/
	UFN_FATAL	=3,		/* function failed unrecoverably */
} UFN_RET;

/* Type for entries in UFN Lookup Table */
typedef	struct	UFN_Spec {
	CONST char 	name[UFN_NAMELEN];			/* name CALLed in KCML	*/
	int		nCall;					/* call number		*/
	UFN_RET		(UFN_API *function)(UFN_Value *);	/* the C function name	*/
	unsigned char	Param[MAXPARAMS]; 			/* info. on parameter	*/
} UFN_Spec;

#define UFN_ARGS	UFN_Value *pb
#define UFN_ARG		pb

#define NVAL(x)		(pb[(x)].nval)
#define IVAL(x)		(pb[(x)].ival)
#define NINT(x)		(IVAL(x))
#define SVAL(x)		(pb[(x)].s.sptr)
#define SLEN(x)		(pb[(x)].s.slen)
#define SATTR(x)	(pb[(x)].s.attr)
#define SYPTR(x)	(pb[(x)].sym.sym_ptr)
#define SYREDIM(x)	(pb[(x)].sym.bRedim)


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
typedef struct	UFN_Subs {
	void	*(*malloc)(int size);		/* malloc		*/
	void	*(*realloc)(void *p, int size);	/* realloc		*/
	void	(*free)(void *p);		/* free			*/
} UFN_Subs;

/* only valid in ufn_ext() and below ( use of -> ) */
#define UFN_MALLOC(x)		(KcmlSubs->malloc(x))
#define UFN_REALLOC(x,y)	(KcmlSubs->realloc(x),(y))
#define UFN_FREE(x)		(KcmlSubs->free(x))

/* type for entry point */
typedef UFN_Spec *(UFN_API *UFN_EXT_FUNC)(UFN_Subs *ptr);
/* prototype for entry point */
UFN_Spec * UFN_API uf_ext(UFN_Subs *p);
