ArrowType (arrow control property)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time<br />
only</td>
<td>Read<br />
only</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (design time only enumerated property)\
*(Right, Left, Down, Up, Right Down, Down Left, Left Up, Up Right, Left Down, Down Right, Right Up, Up Left)*

**Specifies the arrow type and direction**

Use this property to specify what type of arrow to draw.

An example demonstrating all the arrow types is available.

<a href="#nowhere" onclick="CopyTextToClipboard(&#39;EXAMPLE1&#39;)">Copy example to clipboard</a>


    00010 - DEFFORM Form1()=\
              {.form,.form$,.Style=0x50c000c4,.Width=256,.Height=262,.Text$=" Arrow Types",.Id=1024},\
              {.ok,.button$,.Style=0x50010001,.Left=103,.Top=243,.Width=50,.Height=14,.Text$="OK",.__Anchor=5,.Id=1},\
              {.arrowControl1,.arrow$,.Style=0x50018100,.Left=6,.Top=8,.Width=50,.Height=50,.Id=1000,.Alignment=5,.BodyColor=.Blue,.EdgeColor=.Black},\
              {.arrowControl2,.arrow$,.Style=0x50018101,.Left=71,.Top=8,.Width=50,.Height=50,.Id=1001,.Alignment=5,.BodyColor=.Blue,.EdgeColor=.Black},\
              {.arrowControl3,.arrow$,.Style=0x50018102,.Left=137,.Top=8,.Width=50,.Height=50,.Id=1002,.Alignment=5,.BodyColor=.Blue,.EdgeColor=.Black},\
              {.arrowControl4,.arrow$,.Style=0x50018103,.Left=203,.Top=8,.Width=50,.Height=50,.Id=1003,.Alignment=5,.BodyColor=.Blue,.EdgeColor=.Black},\
              {.arrowControl5,.arrow$,.Style=0x50018104,.Left=6,.Top=90,.Width=50,.Height=50,.Id=1004,.BodyColor=.Blue,.EdgeColor=.Black},\
              {.arrowControl6,.arrow$,.Style=0x50018105,.Left=73,.Top=90,.Width=50,.Height=50,.Id=1005,.BodyColor=.Blue,.EdgeColor=.Black},\
              {.arrowControl7,.arrow$,.Style=0x50018106,.Left=137,.Top=90,.Width=50,.Height=50,.Id=1006,.BodyColor=.Blue,.EdgeColor=.Black},\
              {.arrowControl8,.arrow$,.Style=0x50018107,.Left=203,.Top=90,.Width=50,.Height=50,.Id=1007,.BodyColor=.Blue,.EdgeColor=.Black},\
              {.arrowControl9,.arrow$,.Style=0x50018108,.Left=6,.Top=173,.Width=50,.Height=50,.Id=1008,.BodyColor=.Blue,.EdgeColor=.Black},\
              {.arrowControl10,.arrow$,.Style=0x50018109,.Left=71,.Top=174,.Width=50,.Height=50,.Id=1009,.BodyColor=.Blue,.EdgeColor=.Black},\
              {.arrowControl11,.arrow$,.Style=0x5001810a,.Left=137,.Top=173,.Width=50,.Height=50,.Id=1010,.BodyColor=.Blue,.EdgeColor=.Black},\
              {.arrowControl12,.arrow$,.Style=0x5001810b,.Left=203,.Top=174,.Width=50,.Height=50,.Id=1011,.BodyColor=.Blue,.EdgeColor=.Black},\
              {.textControl1,.static$,.Style=0x50000001,.Left=5,.Top=60,.Width=50,.Height=9,.Text$="Right",.Id=1012},\
              {.textControl2,.static$,.Style=0x50000001,.Left=71,.Top=60,.Width=50,.Height=9,.Text$="Left",.Id=1013},\
              {.textControl3,.static$,.Style=0x50000001,.Left=137,.Top=60,.Width=50,.Height=9,.Text$="Down",.Id=1014},\
              {.textControl4,.static$,.Style=0x50000001,.Left=203,.Top=60,.Width=50,.Height=9,.Text$="Up",.Id=1015},\
              {.textControl5,.static$,.Style=0x50000001,.Left=5,.Top=143,.Width=50,.Height=9,.Text$="Right Down",.Id=1016},\
              {.textControl6,.static$,.Style=0x50000001,.Left=71,.Top=143,.Width=50,.Height=10,.Text$="Down Left",.Id=1017},\
              {.textControl7,.static$,.Style=0x50000001,.Left=137,.Top=143,.Width=50,.Height=10,.Text$="Left Up",.Id=1018},\
              {.textControl8,.static$,.Style=0x50000001,.Left=203,.Top=143,.Width=50,.Height=10,.Text$="Up Right",.Id=1019},\
              {.textControl9,.static$,.Style=0x50000001,.Left=5,.Top=226,.Width=50,.Height=9,.Text$="Left Down",.Id=1020},\
              {.textControl10,.static$,.Style=0x50000001,.Left=71,.Top=226,.Width=50,.Height=9,.Text$="Down Right",.Id=1021},\
              {.textControl11,.static$,.Style=0x50000001,.Left=137,.Top=226,.Width=50,.Height=9,.Text$="Right Up",.Id=1022},\
              {.textControl12,.static$,.Style=0x50000001,.Left=203,.Top=226,.Width=50,.Height=9,.Text$="Up Left",.Id=1023}
        : FORM END Form1
        : Form1.Open()
        : $END 

##### See also:

Other [arrow](arrow.htm) properties, methods and events and [generic](generic.htm) properties and methods.
