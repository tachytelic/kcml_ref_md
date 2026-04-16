# uf_json.mak - Build uf_json.so for use with KCML 6.9 UFN (-x flag)
#
# Usage:
#   make -f uf_json.mak
#
# Load with KCML:
#   kcml -x ./uf_json.so -p myscript.kcml

CC      = gcc
CFLAGS  = -O -DUNIX -funsigned-char -fexceptions -fvisibility=hidden -pipe -pthread -m32
LDFLAGS = -shared -Xlinker --as-needed -Xlinker --no-undefined \
          -Xlinker --version-script -Xlinker uf_json.exp -m32

LIBNAME = uf_json.so

$(LIBNAME): uf_json.c uf_pub.h uf_json.exp
	$(CC) $(CFLAGS) -c uf_json.c -o uf_json.o
	$(CC) $(LDFLAGS) -o $(LIBNAME) uf_json.o

clean:
	rm -f $(LIBNAME) uf_json.o
