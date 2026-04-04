Screen colors

Kclient as well as many terminals and PC terminal emulators now support color. So that programs can exploit this technology without being modified a color terminal will define colors for the screen background, normal characters and the attributes of bold and blink. Some terminals will also allow the box graphic colors to be specified.

The HEX(0202 04 *aa bb cc dd ee ff gg*0F) sequence where

|      |                                              |
|------|----------------------------------------------|
| *aa* | Foreground color                             |
| *bb* | Background color                             |
| *cc* | Bold color                                   |
| *dd* | Blink color                                  |
| *ee* | Box color                                    |
| *ff* | Window background (See [WINDOW](WINDOW.htm)) |
| *gg* | Window border (See [WINDOW](WINDOW.htm))     |

allows these characters to be changed under program control. Each color is specified with a letter A to P i.e.

A

Black

I

Grey

B

Blue

J

Bright blue

C

Green

K

Bright green

D

Cyan

L

Bright cyan

E

Red

M

Bright red

F

Magenta

N

Bright magenta

G

Brown

O

Yellow

H

White

P

Bright white

It is not necessary to specify all five color bytes. To discover the colors in use the HEX(0202 043F 0F) sequence will prompt the terminal to reply with 5 bytes describing the current colors and a carriage return. These characters can be read with a [KEYIN](KEYIN.htm) or [LINPUT](LINPUT.htm).

KCML has a certain amount of backward compatibility with the BASIC-2C color model based on CGA technology. The sequence

HEX(0200 0605 *0b 0f 0u 0p 0i* 0F)

where

|      |                          |          |
|------|--------------------------|----------|
| *0b* | background color         | (0 to 7) |
| *0f* | foreground color         | (0 to 7) |
| *0u* | underline color          | (0 to 7) |
| *0p* | border or overscan color | (0 to 7) |
| *0i* | border intensity         | (0 or 1) |

and

|     |         |
|-----|---------|
| 0   | black   |
| 1   | blue    |
| 2   | green   |
| 3   | cyan    |
| 4   | red     |
| 5   | magenta |
| 6   | brown   |
| 7   | white   |

will be honoured on any terminal with the *CGAcolor* and *CGAborder* clauses in its *TERMINFO* file. This command requires that byte 22 of [\$OPTIONS]($OPTIONS.htm#BYTE22) be set to a non-zero value and the terminal initialised with a HEX(020D0C030E) for these sequences to be effective. Bright foreground colors are possible in combination with the bright attribute. The underline color is ignored. If this is required then the *AttribOn* clause should be modified. The border capability is only likely to be found on genuine CGA monitors.
