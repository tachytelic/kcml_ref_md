Introduction to text terminals

Most KCML programs execute under the control of a terminal with a screen on which the program can print information and a keyboard from which it can receive input. On UNIX versions provided that a program does not attempt to read a keyboard then it can run in the background detached from a terminal.

KCML arranges that all terminals look to application programs as if they were a standard 8 bit ASCII terminal with 16 dedicated function keys, four arrow keys and a range of editing keys such as CANCEL, INSERT, DELETE, NEXT, PREV all of which can be shifted. A number of such virtual function keys are defined in KCML for use in [KEYIN](KEYIN.htm), [LINPUT](LINPUT.htm), [LINPUT LINE](LINPUT_LINE.htm), [LINPUT LIST](LINPUT_LIST.htm) and the program editor. The function keys are additional to the 256 possible ordinary keys and will usually be multi-character sequences. The 16 dedicated keys are labelled 0 to 15, and 16 to 31 when shifted. The [KEYIN](KEYIN.htm) statement reports this number as the value of the character and can jump to a different line number to signify that the key is a function key. The following editing keys return similar higher numbers:

|            |        |            |
|------------|--------|------------|
| AUTOINSERT | INSERT | SELECTMODE |
| CANCEL     | NEXT   | SOUTH      |
| DELETE     | NORTH  | WEST       |
| EAST       | PASTE  |            |
| EXECUTE    | PREV   |            |
