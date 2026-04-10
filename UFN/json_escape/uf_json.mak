# uf_json.mak - Build uf_json.so for use with KCML UFN (-x flag)
#
# Usage:
#   make -f uf_json.mak
#
# Output:
#   uf_json.so
#
# Load with KCML:
#   kcml -x ./uf_json.so -p pik_to_json.kcml <db_dir> <pik_note>

CC      = gcc
# Add -m32 only on 64-bit hosts (Ubuntu 8.04 is native 32-bit, no flag needed)
ARCH    := $(shell uname -m)
M32     := $(if $(filter x86_64,$(ARCH)),-m32,)
CFLAGS  = -O -DUNIX -fPIC -Wall $(M32)
LDFLAGS = -shared

LIBNAME = uf_json.so

$(LIBNAME): uf_json.c uf_pub.h
	$(CC) $(CFLAGS) $(LDFLAGS) -o $(LIBNAME) uf_json.c

clean:
	rm -f $(LIBNAME)
