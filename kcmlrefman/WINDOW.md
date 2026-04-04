WINDOW

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/window.gif" data-align="BOTTOM" data-border="0" alt="window.gif" />\
\
Where:\
\
     title                     = alpha_variable, literal_string\
\
     window_no                = a numeric expression in the range 0-9\
\
     depth, width, row, column           = a numeric expression\
\

------------------------------------------------------------------------

The WINDOW statement is used to open windows on the screen restoring the original screen when the window is closed. This statement is only relevant to text based applications.

On KCML terminals the text and box graphics behind the window are stored in the memory of the terminal until the window is closed again. On other terminals this is performed by KCML. Up to 10 windows can be held on the screen at any one time. If more than one window is opened then each window should have a different window number after the \`#' sign. If no window number is used, a default of \#0 is assumed. Each window may have a centred title of up to 78 characters. If the title variable is absent then no border is drawn. After a window is opened the window area is cleared to the background color and the cursor is automatically positioned to the top left of the window and turned off. While a window is active the cursor is not constrained to the window area and therefore text can be written anywhere on the physical screen. Windows do not scroll when text is written below the last line.

To open a window titled \`Window number one', of size 15 by 20, at the top left hand corner of the screen, the following statement should be issued

WINDOW OPEN \#1, "Window number one",15,20 AT(0,0)

Windows are removed using the WINDOW CLOSE statement. This restores the text hidden by the window and resets the cursor back to its previous position and style. The current screen attribute is also restored but the color palette is not. Because windows can overlap, they must be removed in the reverse order to which they were placed. If no window number is specified after the WINDOW CLOSE statement, a default of \#0 is assumed. If the ALL keyword is specified after the WINDOW CLOSE statement, all currently open windows are closed in descending order, e.g. \#4 to \#0, irrespective of the order in which they were opened. To remove the window placed by the previous example, the following would be used:

WINDOW CLOSE \#1

The KCML 5.03 kclient has the ability to display these text windows as pop-up forms. This is controlled by a checkbox in the client's Text Preferences dialog. It is enabled by default.

Syntax examples:

WINDOW OPEN "Main Window" 5,20 AT(5,0)\
WINDOW OPEN \#1, title\$, 10, 10 AT(5,5)\
WINDOW OPEN \#no, title\$, sz(1), sz(2) AT(row,column)\
WINDOW CLOSE\
WINDOW CLOSE ALL\
WINDOW CLOSE \#window_number

See also:

[INPUT SCREEN](INPUT_SCREEN.htm), [PRINT SCREEN](PRINT_SCREEN.htm)
