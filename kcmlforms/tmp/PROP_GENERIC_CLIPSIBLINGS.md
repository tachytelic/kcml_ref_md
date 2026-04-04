ClipSiblings (generic control property)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time<br />
only</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (design time only boolean property)

**Controls how overlapping controls are treated**

If two controls on a form overlap then how the intersection is painted is determined by this style. If set to FALSE each control will paint the whole of its surface redrawing the intersectional area. If set TRUE then the intersection is clipped and the Z-order (effectively the tab order) of the controls will determine which control paints the intersection.

This is a design time only style. There is no effect if set or inspected at run time.

For Windows NT, Windows 2000 and Windows 9x this style is off by default. Enabling this style will result is a slower screen draw so it should be left off unless you really do need the feature. On the Windows CE kclient this style is always set (CE provides no mechanism to turn it off).

This style only matters if controls overlap. It concerns only sibling controls on the same form. Dependency on overlapping controls is discouraged as this style may not be programmable in future versions of KClient.

Here is an example program illustrating overlapping buttons. Buttons are redrawn whenever they are clicked. To execute the example program in KCML simply click <a href="#nowhere" onclick="CopyTextToClipboard(&#39;PicDiv&#39;)">here</a> to copy the program into the clipboard switch to the KCML Workbench, clear out any existing code and press Ctrl+V to paste the example into the program. - DEFFORM Form1()={.form,.form\$,.Style=0x50c000c\\ 4,.Width=216,.Height=111,.text\$="ClipSiblings ex\\ a\\ mple",.Id=1024},{.ok,.button\$,.Style=0x50010001,\\ .Left=160,.Top=6,.Width=50,.Height=14,.text\$="OK\\ "\\ ,.\_\_Anchor=5,.Id=1},{.cmdButton1,.button\$,.Style\\ =0x50010000,.Left=12,.Top=4,.Width=48,.Height=14\\ ,\\ .text\$="FALSE",.Id=1000},{.cmdButton2,.button\$,.\\ Style=0x50010000,.Left=50,.Top=9,.Width=48,.Heig\\ h\\ t=14,.text\$="FALSE",.Id=1001},{.cmdButton3,.butt\\ on\$,.Style=0x50010000,.Left=12,.Top=28,.Width=48\\ ,\\ .Height=14,.text\$="FALSE",.Id=1002},{.cmdButton4\\ ,.button\$,.Style=0x54010000,.Left=50,.Top=33,.Wi\\ d\\ th=48,.Height=14,.text\$="TRUE",.Id=1003},{.cmdBu\\ tton5,.button\$,.Style=0x54010000,.Left=11,.Top=5\\ 1\\ ,.Width=48,.Height=14,.text\$="TRUE",.Id=1004},{.\\ cmdButton6,.button\$,.Style=0x50010000,.Left=50,.\\ T\\ op=57,.Width=48,.Height=14,.text\$="FALSE",.Id=10\\ 05},{.cmdButton7,.button\$,.Style=0x54010000,.Lef\\ t\\ =11,.Top=75,.Width=48,.Height=14,.text\$="TRUE",.\\ Id=1006},{.cmdButton8,.button\$,.Style=0x54010000\\ ,\\ .Left=49,.Top=81,.Width=48,.Height=14,.text\$="TR\\ UE",.Id=1007} FORM END Form1 Form1.Open()

##### See also:

Other [generic](generic.htm) properties, methods and events and [generic](generic.htm) properties and methods.
