Type (graph control property)

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
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
5.03+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Enumerated property\
*(Pie, Bar, Pie3D, Bar3D, Line)*

**Graph type**

The graph **Type** property sets the style of the graph to be displayed. Currently three types are supported: bars, lines and pie charts in 2D and 3D styles. The bar and line charts support single or multiple data sets, but the pie charts will only show a single pie with the first data set. The 3D styles are identical to the 2D styles except they show pie sections and bar elements with 3D shading. There are no perspective or rotation options in 3D.

An example demonstrating all the graph types is available.

<a href="#nowhere" onclick="CopyTextToClipboard(&#39;EXAMPLE1&#39;)">Copy example to clipboard</a>


    00020 - DEFFORM Form1()=\
              {.form,.form$,.Style=0x50c400c4,.Width=434,.Height=353,.Text$="Form",.Id=1024,.Placement=15},\
              {.Line,.radio$,.Style=0x50010004,.Left=375,.Top=177,.Width=50,.Height=13,.Text$="&Line",.__Anchor=4,.Id=1007,.ButtonGroup=.Style},\
              {.ok,.button$,.Style=0x50010001,.Left=375,.Top=6,.Width=50,.Height=14,.Text$="OK",.__Anchor=5,.Id=1},\
              {.cancel,.button$,.Style=0x50010000,.Left=375,.Top=23,.Width=50,.Height=14,.Text$="Cancel",.__Anchor=5,.Id=2},\
              {.help,.button$,.Style=0x50010000,.Left=375,.Top=44,.Width=50,.Height=14,.Text$="&Help",.__Anchor=5,.Id=9},\
              {.graph,.graph$,.Style=0x50010000,.Left=21,.Top=11,.Width=330,.Height=332,.Text$="Graph Demonstration",.__Anchor=15,.Id=1001},\
              {.Pie,.radio$,.Style=0x50010004,.Left=375,.Top=194,.Width=50,.Height=13,.Text$="&Pie",.__Anchor=4,.Id=1002,.State=1,.ButtonGroup=.Style},\
              {.Bar,.radio$,.Style=0x50010004,.Left=375,.Top=214,.Width=50,.Height=13,.Text$="&Bar",.__Anchor=4,.Id=1003,.ButtonGroup=.Style},\
              {.Pie1,.radio$,.Style=0x50010004,.Left=375,.Top=234,.Width=50,.Height=13,.Text$="&Pie 3D",.__Anchor=4,.Id=1000,.ButtonGroup=.Style},\
              {.Bar1,.radio$,.Style=0x50010004,.Left=375,.Top=254,.Width=50,.Height=13,.Text$="&Bar 3D",.__Anchor=4,.Id=1004,.ButtonGroup=.Style}
        :     + DEFEVENT Form1.Enter()
        :         LOCAL DIM i
        :         OBJECT b = Form1.graph
        :         FOR i = 1 TO 16
        :             b.Data(0,i,1.7*i*i-20)
        :             b.Data(1,i,i*i*i/10+40)
        :             b.XLabel(i,BIN(VAL("A")+i-1))
        :         NEXT i
        :         .graph.Type = &.Pie
        :     END EVENT
        :     + DEFEVENT Form1.Pie.Click()
        :         .graph.Type = &.Pie
        :     END EVENT
        :     + DEFEVENT Form1.Bar.Click()
        :         .graph.Type = &.Bar
        :     END EVENT
        :     + DEFEVENT Form1.Pie1.Click()
        :         .graph.Type = &.Pie3D
        :     END EVENT
        :     + DEFEVENT Form1.Bar1.Click()
        :         .graph.Type = &.Bar3D
        :     END EVENT
        :     + DEFEVENT Form1.Line.Click()
        :         .graph.Type = &.Line
        :     END EVENT
        :     + DEFEVENT Form1.graph.Click()
        :         .help.Text$ = ..ClickIndex & "," & ..ClickSet
        :         ..Explode(..ClickSet,..ClickIndex,TRUE)
        :     END EVENT
        :     
        : FORM END Form1
        : Form1.Open()
        : 

##### Example:


     .graphControl.Type = &.Pie

##### See also:

Other [graph](graph.htm) properties, methods and events and [generic](generic.htm) properties and methods.
