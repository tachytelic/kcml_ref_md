# uf_json_parse.mak - Build uf_json_parse.so for use with KCML 6.9 UFN (-x flag)
#
# Requires: libcjson-dev:i386  (32-bit cJSON headers + library)
#   sudo apt-get install libcjson-dev:i386
#
# Usage:
#   make -f uf_json_parse.mak
#
# Load with KCML:
#   kcml -x ./uf_json_parse.so -p myscript.kcml

CC      = gcc
CFLAGS  = -O -DUNIX -funsigned-char -fexceptions -fvisibility=hidden -pipe -pthread -m32
LDFLAGS = -shared -Xlinker --as-needed -Xlinker --no-undefined \
          -Xlinker --version-script -Xlinker uf_json_parse.exp -m32

LIBNAME = uf_json_parse.so

$(LIBNAME): uf_json_parse.c cJSON.c cJSON.h uf_pub.h uf_json_parse.exp
	$(CC) $(CFLAGS) -c uf_json_parse.c -o uf_json_parse.o
	$(CC) $(CFLAGS) -c cJSON.c -o cJSON.o
	$(CC) $(LDFLAGS) $(CFLAGS) -o $(LIBNAME) uf_json_parse.o cJSON.o

clean:
	rm -f $(LIBNAME)
