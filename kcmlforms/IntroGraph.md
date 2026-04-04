An introduction to the Graph Control

------------------------------------------------------------------------

Graph controls are added to forms at design time using the [Forms Designer](FormsDesignerWorkingWithGraphs.htm).

The control supports various 2D and 3D pie and bar graph presentations through the [.Type](tmp/PROP_GRAPH_TYPE.htm) enumeration. This can be set at design time as can the grpah title which is set with the generic [.Text\$](tmp/PROPSTR_TITLE.htm) property. Graphs can have [legends](tmp/PROP_GRAPH_LEGEND.htm) and the X axis can be [labelled](tmp/PROP_GRAPH_XLABEL.htm). These are set at runtime by method calls.

A graph supports potentially more than one data set numbered with numeric labels. This is to allow for the possibility of stacked bars which will be displayed with each data set in a different color. Pie charts only ever use the first data set. Within each data set there are a number of data points identified by index numbers. Both index numbers and data set numbers are arbitrary small integers. You can count from zero or from one and leave gaps in the sequence as you please.

The [Data(ds, i, amp)](tmp/PROP_GRAPH_DATA.htm) and [Data(i, amp)](tmp/PROP_GRAPH_DATA2.htm) methods are used to set the data to be displayed. There are two variants as the dataset number is not required for pie charts. The [Reset()](tmp/PROP_GRAPH_RESET.htm) method will drop any data, labels and legent text associated with the graph.

Graphs can be 'hot' supporting a [.Click()](tmp/PROP_GRAPH_CLICK.htm) event if the user clicks on a particular pie segment or bar. The [.ClickSet](tmp/PROP_GRAPH_CLICKSET.htm) and [.ClickIndex](tmp/PROP_GRAPH_CLICKINDEX.htm) properties can then be examined to see which datum was clicked. Right clicking on a graph will temporarily flip the graph type between bar and pie.

Pie segments can also be exploded using the [.Explode()](tmp/PROP_GRAPH_EXPLODE.htm) method.

OBJECT notation can be used with graph controls. The object does exist and can be referenced this way at the time of the Enter() event. For example OBJECT b = Form1.graph

For a complete list of the methods, properties and events supported see the [control summary](tmp/graph.htm) in this section.

The KCML Graph Control was added for KCML 5.03 and enhanced for KCML 6.00. For compatibility issues with the GraphServer OCX see the [compatibility notes](GraphCompat.htm).

An example KCML program showing all the available graph types can be found under the [.Type](tmp/PROP_GRAPH_TYPE.htm) documentation.
