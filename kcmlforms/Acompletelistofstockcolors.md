A complete list of stock colors

------------------------------------------------------------------------

The following is a complete list of the stock colors available. These colors can be used to change the background and text colors of a control by assigning them to the [BackColor](tmp/PROP_GENERIC_BACKCOLOUR.htm) and [TextColor](tmp/PROP_GENERIC_TEXTCOLOUR.htm) properties. These colors can be assigned both at design time within the Forms Designer or under program control. For example, the following would change the background and text colors of the edit control:

.editControl1.BackColor = &.Cyan .editControl1.TextColor = &.DarkBlue

|  |  |
|----|----|
| Black | <img src="bitmaps/stock_color_e.gif" data-border="0" alt="stock_color_e.gif" />  |
| Blue | <img src="bitmaps/stock_color_1.gif" data-border="0" alt="stock_color_1.gif" />  |
| DarkBlue | <img src="bitmaps/stock_color_2.gif" data-border="0" alt="stock_color_2.gif" />  |
| Brown | <img src="bitmaps/stock_color_3.gif" data-border="0" alt="stock_color_3.gif" />  |
| Cyan | <img src="bitmaps/stock_color_4.gif" data-border="0" alt="stock_color_4.gif" />  |
| DarkCyan | <img src="bitmaps/stock_color_5.gif" data-border="0" alt="stock_color_5.gif" />  |
| Default |   |
| Gray | <img src="bitmaps/stock_color_6.gif" data-border="0" alt="stock_color_6.gif" />  |
| DarkGray | <img src="bitmaps/stock_color_7.gif" data-border="0" alt="stock_color_7.gif" />  |
| Green | <img src="bitmaps/stock_color_8.gif" data-border="0" alt="stock_color_8.gif" />  |
| DarkGreen | <img src="bitmaps/stock_color_9.gif" data-border="0" alt="stock_color_9.gif" />  |
| Magenta | <img src="bitmaps/stock_color_10.gif" data-border="0" alt="stock_color_10.gif" />  |
| DarkMagenta | <img src="bitmaps/stock_color_11.gif" data-border="0" alt="stock_color_11.gif" />  |
| Red | <img src="bitmaps/stock_color_12.gif" data-border="0" alt="stock_color_12.gif" />  |
| DarkRed | <img src="bitmaps/stock_color_13.gif" data-border="0" alt="stock_color_13.gif" />  |
| White | <img src="bitmaps/stock_color_14.gif" data-border="0" alt="stock_color_14.gif" />  |
| Yellow | <img src="bitmaps/stock_color_15.gif" data-border="0" alt="stock_color_15.gif" />  |

The following stock background colors are set by the user in the [form preferences](mk:@MSITStore:kclient.chm::/formprefs.htm) property tab of the client. It is the color currently in effect for this purpose that is used.

|              |                                                |
|--------------|------------------------------------------------|
| Edit         | Used for editable fields in DbEdits and grids  |
| EditReadOnly | Used for read-only fields in DbEdits and grids |

The first two of these background stock colors can be set by the user in the [Currency preferences](mk:@MSITStore:kclient.chm::/altcurrsupport.htm) property tab of the client.

|  |  |
|----|----|
| CurrencyEdit | Background color chosen in Preferences for an editable alternate currency |
| CurrencyEditReadOnly | Background color chosen in Preferences for a read-only alternate currency |
| ConvertedEdit | Background color used for a editable alternate currency when converted into the alternate currency by the user clicking the currency button on the title bar |
| ConvertedEditReadOnly | As above but for read-only fields |

These stock colors are set using the display applet in the Windows control panel

|  |  |
|----|----|
| Face | The color used for the face of buttons and the background color of dialogs |

This stock color varies according to the context of the control. It was introduced in KCML 6.00.

|  |  |
|----|----|
| Background | The background color of the item that the control is on (frame control, tab control or the entire dialog). This is similar to making a control transparent, but more efficient as the control is still colored. |

##### See also:

[A complete list of stock fonts](Acompletelistofstockfonts.htm)\
[A complete list of stock pictures](Acompletelistofstockpics.htm)\
[BackColor (property)](tmp/PROP_GENERIC_BACKCOLOUR.htm)\
[TextColor (property)](tmp/PROP_GENERIC_TEXTCOLOUR.htm)
