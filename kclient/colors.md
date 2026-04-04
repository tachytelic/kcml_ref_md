# <span id="colors"></span> Colors

The standard KCML text color scheme allows attributes such as blink and bright to be represented by different colors. It is also possible for the application to specify a specific color for the foreground and background of a text cell. In this case the user cannot affect the look of the program. This dialog can only control text mode programs using attribute mapping.

You can control the color of the following elements

| Element | Purpose |
|----|----|
| Text | Foreground text |
| Background | The background color for a text cell |
| Bright | The color to be used for the bright attribute |
| Blink | The color to be used for the blink attribute |
| Box | The color of box graphic lines |
| Window background | The background of a popup window (see [WINDOW](mk:@MSITStore:kcmlrefman.chm::/WINDOW.htm) statement) |
| Window border | The edging of a popup window |
| Window text | The color of the text within a popup window |

As colors are changes an example in the bottom left of the dialog will be updated to show that change.

Colors are set using a palette model whereby a color letter A to P stands for one of 16 basic RGB colors. The actual color represented by the letter can be changed however to a specific hue using a Customize Color dialog. Another button will restore the defaults.
