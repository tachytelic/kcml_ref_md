VT220 sequences

The following table shows the escape sequences that can be used for programming in VT220 mode. Eight bit CSI and SS3 sequences are also supported. Sequences in italic are accepted but have no effect or are unimplemented.

Note that any VT220 escape sequence can be used during [KCML emulation](TextSeqDW.htm) by prefixing the sequence with the character HEX(02).

VT100 specific sequences

Escape Codes

Description

NUL

Ignored

ENQ

Sends answerback

BEL

Generates a bell tone

BS

Non destructive backspace. If at left margin no action occurs

HT

Move to next tab stop or right margin if there are no more. Does not cause autowrap

LF

Causes line feed or new line depending on mode

VT

Processed as LF

FF

Processed as LF

SO

Invokes G1 character set into GL

SI

Invokes G0 character set into GL

CAN

Cancels any escape sequence

DEL

Ignored

ESC =

Sets the keypad to application mode

ESC \>

Sets the keypad to numeric mode

ESC 7

Saves the cursor position, attributes and character set

ESC 8

Restores the cursor position, attributes and character set

ESC D

Moves the cursor down one line

ESC E

Moves the cursor to the first position one line down

ESC H

Sets a tab stop at current column

ESC M

Reverse index. Moves the cursor up one line in same column

ESC N

Temporarily invokes G2 character set into GL for the next character

ESC O

Temporarily invokes G2 character set into GL for the next character

ESC c

Resets the terminal

ESC g

Clears tab stop at current column

ESC \# 3

*Double height line (top half)*

ESC \# 4 

*Double height line (bottom half)*

ESC \# 5

*Single width line*

ESC \# 6 

*Double width line*

ESC \# 8 

Fills the entire screen with E's (screen alignment test)

ESC ( 0 

Selects the graphics character set for G0

ESC ) 0 

Selects the graphics character set for G1

ESC ( A 

Selects the UK character set for G0

ESC ) A 

Selects the UK character set for G1

ESC ( B 

Selects the ASCII character set for G0

ESC ) B 

Selects the ASCII character set for G1

ESC \[ ? n;...;n h

Sets one or more mode(s)\
                        1 = cursor keys in application mode\
                        2 = VT52 mode off\
                        3 = 132 column on\
                        4 = smooth scrolling on\
                        5 = reverse video screen\
                        6 = scrolling region origin mode on\
                        7 = auto wrap on\
                        8 = auto repeat on\
                        25 = cursor on\
                        70 = switch to KCML emulation\
                        80 = switch to KCML emulation\

ESC \[ ? i

Dump screen to printer

ESC \[ ? 1 i

*Print line containing the cursor*

ESC \[ ? 4 i

Turns off autoprint mode

ESC \[ ? 5 i

Turns on autoprint mode

ESC \[ ? n;...;n l

Resets one or more mode(s)\
                        1 = cursor keys in cursor mode\
                        2 = VT52 mode on\
                        3 = 80 column on\
                        *4 = jump scrolling on*\
                        5 = normal video screen\
                        6 = screen origin mode on\
                        7 = autowrap off\
                        *8 = auto repeat off*\
                        25 = cursor off\
                        70 = switch to VT220 emulation\
                        80 = switch to VT220 emulation

ESC \[ n A

Moves the cursor up n lines

ESC \[ n B

Moves the cursor down n lines

ESC \[ n C

Moves the cursor n positions to the right

ESC \[ n D

Moves the cursor n positions to the left

ESC \[ r;c H

Positions the cursor at row r, column c

ESC \[ r;c f

As above

ESC \[ n J

Erases all or part of the screen.\
                        0 = erases from current position to end of screen\
                        1 = erases from start of screen to current position\
                        2 = erases complete display

ESC \[ n K

Erases all or part of a line.\
                        0 = erases from current column to end of line\
                        1 = erases from start of line to current column\
                        2 = erases entire line

ESC \[ c

Returns the terminal identification screen

ESC \[ n g

Clears tab or all tabs depending on parameter

ESC \[ n;...;n h

Sets one or more mode(s)\
                        *2 = keyboard locked*\
                        4 = insert mode on\
                        *12 = send/receive on*\
                        20 = new line mode

ESC \[ 4 i

Revert output to screen

ESC \[ 5 i

Divert output to local printer

ESC \[ n;...;n l

Resets one or more mode(s)\
                        *2 = keyboard unlocked*\
                        4 = insert mode off\
                        *12 = send/receive off*\
                        20 = line feed new line mode

ESC \[ n;...;n m

Selects the character attributes:\
                        0 or none = all attributes off\
                        1 = bold\
                        4 = underline\
                        5 = blink\
                        7 = reverse video

ESC \[ n n

Returns device status or cursor position\
                        5 = "What is your status"\
                        6 = "What is your cursor position"\
                        15 = "What is the printer status"\
                        25 = "What is the user defined key status"

ESC \[ t;b r

Sets the top and bottom margins. Lines are counted from 1

ESC \[ n;m " p

Set the emulation/compatibility level 61= Set terminal to VT100 62= Set terminal to VT220, 8 bit 62;0= Set terminal to VT220, 8 bit 62;1= Set terminal to VT220, 7 bit 62;2= Set terminal to VT220, 8 bit

ESC \[ ! p

Soft terminal reset

VT220 specific sequences

| Escape Code | Description                                |
|-------------|--------------------------------------------|
| ESC \[ n L  | Inserts n lines at the cursor              |
| ESC \[ n M  | Deletes n lines at the cursor              |
| ESC \[ n @  | Insert n blank characters at the cursor    |
| ESC \[ n P  | Deletes n characters at the cursor         |
| ESC \* B    | Designate ASCII character set as G2        |
| ESC + B     | Designate ASCII character set as G3        |
| ESC ( \<    | Invoke multinational character set into G0 |
| ESC ) \<    | Invoke multinational character set into G1 |
| ESC \* \<   | Invoke multinational character set into G2 |
| ESC + \<    | Invoke multinational character set into G3 |
| ESC \* O    | Designate graphics character set as G2     |
| ESC + O     | Designate graphics character set as G3     |
| ESC n       | Invoke G2 into GL                          |
| ESC o       | Invoke G3 into GL                          |
| ESC ~       | Invoke G1 into GR                          |
| ESC }       | Invoke G2 into GR                          |
| ESC \|      | Invoke G3 into GR                          |

ANSI specific sequences

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Escape Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>ESC [ n S</td>
<td>Scroll region up n lines, starting from cursor position</td>
</tr>
<tr>
<td>ESC [ n T</td>
<td>Scroll region down n lines, starting from cursor position</td>
</tr>
<tr>
<td>ESC [ n X </td>
<td>Erases n characters from cursor position</td>
</tr>
<tr>
<td>ESC [ n Z</td>
<td>Moves cursor position back n tab stops</td>
</tr>
<tr>
<td>ESC [ s</td>
<td>save cursor position</td>
</tr>
<tr>
<td>ESC [ u</td>
<td>restore cursor position</td>
</tr>
<tr>
<td>ESC [ n;..m</td>
<td>Set foreground/background Colors, where n is<br />
                        30 = black foreground<br />
                        31 = red foreground<br />
                        32 = green foreground<br />
                        33 = yellow foreground<br />
                        34 = blue foreground<br />
                        35 = magenta foreground<br />
                        36 = cyan foreground<br />
                        37 = white foreground<br />
                        40 = black background<br />
                        41 = red background<br />
                        42 = green background<br />
                        43 = yellow background<br />
                        44 = blue background<br />
                        45 = magenta background<br />
                        46 = cyan background<br />
                        47 = white background</td>
</tr>
</tbody>
</table>
