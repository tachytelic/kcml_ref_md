<?xml version="1.0"?>
<!-- $Id: pan.xsl,v 1.20 2009/07/03 14:17:55 rmaun Exp $ -->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/1999/xhtml">
	<xsl:template match="/">
		<html><head>
		<title><xsl:call-template name="title"/></title>
		<style>
p, body, table { background-color: white; color: black; font-family: Verdana, Arial, Helvetica, sans-serif; font-size: 8pt; }
table	{ text-align: left; }
th	{ background-color: #DDDDDD; padding-right: 10px; }
td	{ background-color: #EEEEEE; }
pre	{ background-color: wheat; padding-top: 1em; padding-bottom: 1em; padding-left: 10px; padding-right: 10px; font-size: 10pt; }
ul	{ cursor: pointer; }
		</style>
	</head><body>
<script>

function clearTable(tbody)
{
	while (tbody.rows.length != 0)
		tbody.deleteRow(0);
}

function setcell(tr, text)
{
	var	td;
	var	x;

	// innerHTML throws exception on FF 1.0
	td = tr.insertCell(tr.cells.length);
	x = document.createTextNode(text);
	td.appendChild(x);
}

function ToggleVars(divID, idivID, filter)
{
	var		re;
	var		len;
	var		i;
	var		o;
	var		tr, td;
	var		div;
	var		tbody;

	div = document.getElementById(divID);
	tbody = document.getElementById('vars');
	clearTable(tbody);
	if (filter || div.style.display == 'none') {
		window.status ="Building table ";
		if (filter == '')
			filter = null;
		if (filter)
			re = new RegExp(filter, "i");
		len = olist.items.length;
		for (i=0; i != len; i++) {
			o = olist.items[i];
			if (filter) if (o.name.search(re) == -1)
				continue;
			tr = tbody.insertRow(tbody.rows.length);
			setcell(tr, o.type);
			setcell(tr, o.name);
			setcell(tr, o.value);
			if (i % 256 == 0)
				window.status += '.';
		}
		window.status = "";
		div.style.display = 'block';
	}
	else {
		div.style.display = 'none';
	}
}

function HideDiv(divid)
{
	document.getElementById(divid).style.display = 'none';
}

function ToggleDiv(divid)
{
	var	elem;

	elem = document.getElementById(divid);
	if (elem.style.display == 'none') {
		elem.style.display = 'block';
	}
	else {
		elem.style.display = 'none';
	}
}

function ToggleRecord(levent, divid)
{
	var	div;

	div = document.getElementById(divid);
	if (div.style.display == "none") {
		div.style.display = "block";
	}
	else {
		div.style.display = "none";
	}
	if (levent.stopPropagation) {
		levent.stopPropagation();
	}
	levent.cancelBubble = true;
}

function FilterVars(divID, idivID, filter)
{
	document.getElementById(divID).style.display = 'none';
	ToggleVars(divID, idivID, filter);
}

// variable object constructor
function VarObj(type, name, valueattr, value)
{
	this.type = type;
	this.name = name;
	this.value = (valueattr ? valueattr : value);
}

// list constructor
function VarList()
{
	this.items = new Array();
	this.addItem = addNewVarItem;
}

function addNewVarItem(item)
{
	this.items[this.items.length] = item;
}
var olist = new VarList();
<xsl:for-each select="//sections/variables/*">
	olist.addItem(new VarObj('<xsl:value-of select="@type"/>',<xsl:call-template name="fmtname"/>,'<xsl:value-of select="@value"/>','<xsl:value-of select="text()"/> '));
</xsl:for-each>
</script>
		<h2><xsl:call-template name="title"/></h2>
		<xsl:apply-templates select="//basics"/>
		<ul>
			<xsl:apply-templates select="//sections/*"/>
		</ul>
		</body></html>
	</xsl:template>

	<xsl:template match="basics">
		<table>
		<xsl:for-each select="./*">
		<xsl:if test="text()">
		<tr>
			<th><xsl:value-of select="name()"/></th>
			<td><xsl:value-of select="text()"/></td>
		</tr>
		</xsl:if>
		</xsl:for-each>
		</table>
	</xsl:template>

	<!-- connection handles -->
	<xsl:template match="connect">
		<xsl:call-template name="menulist"/>
		<div><xsl:call-template name="startdiv"/>
		<table>
		<tr>
		<th>Connection</th>
		<th>Type</th>
		<th>DSN</th>
		<th>State</th>
		<th>Last error</th>
		</tr>
		<xsl:for-each select="./chand">
		<tr>
			<td><xsl:value-of select="./cno"/></td>
			<td><xsl:value-of select="./type" /></td>
			<td><xsl:value-of select="./dsn" /></td>
			<td><xsl:value-of select="./state" /></td>
			<td><xsl:value-of select="./errno" />
				<xsl:if test="./errtxt">
					<br/><xsl:value-of select="./errtxt" />
				</xsl:if>
			</td>
		</tr>
		</xsl:for-each>
		</table>
		</div>
	</xsl:template>

	<!-- DB handles -->
	<xsl:template match="handle">
		<xsl:call-template name="menulist"/>
		<div><xsl:call-template name="startdiv"/>
		<table>
		<tr>
		<th>Handle</th>
		<th>Connection</th>
		<th>State</th>
		<th>Table name</th>
		<th>Type</th>
		<th>Reclen</th>
		<th>Mode</th>
		<th>Path</th>
		<th>Last error</th>
		</tr>
		<xsl:for-each select="./hand">
		<tr>
			<td><xsl:value-of select="./hno"/></td>
			<td><xsl:value-of select="./cno"/></td>
			<td><xsl:value-of select="./state" /></td>
			<td><xsl:value-of select="./name" /></td>
			<td><xsl:value-of select="./type" /></td>
			<td><xsl:value-of select="./reclen" /></td>
			<td><xsl:value-of select="./mode" /></td>
			<td><xsl:value-of select="./path" /></td>
			<td><xsl:value-of select="./errno" />
				<xsl:if test="./errtxt">
					<br/><xsl:value-of select="./errtxt" />
				</xsl:if>
			</td>
		</tr>
		</xsl:for-each>
		</table>
		</div>
	</xsl:template>

	<!-- system information, $PSTAT, $VERSION etc -->
	<xsl:template match="sysinfo">
		<xsl:call-template name="menulist"/>
		<div><xsl:call-template name="startdiv"/>
		<table>
		<xsl:for-each select="./*">
		<tr>
			<th><xsl:value-of select="name()"/></th>
			<td><xsl:value-of select="text()" /></td>
		</tr>
		</xsl:for-each>
		</table>
		</div>
	</xsl:template>

	<!-- Command line params -->
	<xsl:template match="args">
		<xsl:call-template name="menulist"/>
		<div><xsl:call-template name="startdiv"/>
		<xsl:for-each select="./arg">
			<xsl:value-of select="text()" />
			<xsl:text> </xsl:text> 
		</xsl:for-each>
		</div>
	</xsl:template>

	<xsl:template match="environ|localenv">
		<xsl:call-template name="menulist"/>
		<div><xsl:call-template name="startdiv"/>
		<table>
		<tr><th>Name</th><th>Value</th></tr>
		<xsl:for-each select="./*">
		<tr>
			<td><xsl:value-of select="@name" /></td>
			<td><xsl:value-of select="text()"/></td>
			<xsl:if test="@value">
				<td><xsl:value-of select="@value" /></td>
			</xsl:if>
		</tr><xsl:text>
		</xsl:text>
		</xsl:for-each>
		</table>
		</div>
	</xsl:template>
	
	<!-- Record Stuff pulled in from webform.xslt -->
	
	<xsl:template name="do_fld_col">
		<td class='fldcol'>
			<b><xsl:call-template name='symbol_name' /></b>
			<xsl:call-template name='nodetype' />
		</td>
	</xsl:template>

	<!-- Print symbol name --> 
	<xsl:template name='symbol_name'>
		<span class="symbol"><xsl:value-of select='@name' /></span>
	</xsl:template>

	<!-- Print type info -->
	<xsl:template name='nodetype'>
		<xsl:if test='@type !=""'>
			<span class="keyword"> AS </span><span class="type"><xsl:value-of select='@type' /></span>
		</xsl:if>
	</xsl:template>

	<xsl:template name='do_record_fld'>
		<xsl:if test='count(./fld) != 0'>
			<xsl:for-each select='./fld'>
				<tr>
					<xsl:call-template name='do_fld_col' />
					<td><xsl:apply-templates /></td>
				</tr><xsl:text>
				</xsl:text>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>	

	<xsl:template name='do_record_body'>
		<xsl:if test='count(./inherits) != 0'>
			<xsl:for-each select='./inherits'>
				<xsl:call-template name='do_record_body' />
			</xsl:for-each>
		</xsl:if>
		<xsl:call-template name='do_record_fld' />
	</xsl:template>	

	<!-- Record instance -->
	<xsl:template match='record'>
		<xsl:variable name="DivName1" select="concat('ShowDiv_', @name, '_', generate-id(), '_', position())" />
		<xsl:variable name="Toggle">ToggleRecord(event, '<xsl:value-of select='$DivName1' />');</xsl:variable>

		<xsl:if test='count(./*) != 0'>
			<span onmouseover='style.color="red"' onmouseout='style.color=""'>
				<xsl:attribute name='onclick'><xsl:value-of select='$Toggle' /></xsl:attribute>
				<u>Toggle field(s)</u>
				<div>
					<xsl:attribute name='id'><xsl:value-of select='$DivName1' /></xsl:attribute>
					<xsl:attribute name="style">display: none;</xsl:attribute>
					<table>
						<xsl:call-template name='do_record_body' />
					</table>
				</div>
			</span>
		</xsl:if>
	</xsl:template>

	<xsl:template match="new_stack">
		<xsl:call-template name="menulist"/>
		<div><xsl:call-template name="startdiv"/>

		<xsl:for-each select="./level">
			<h3>
				<xsl:value-of select="@text" />
				
				<xsl:if test="@index > 0">
					&#160;@&#160;<xsl:value-of select="@filename" />
					,
					&#160;line&#160;<xsl:value-of select="@lineno" />
					,
					&#160;statement&#160;<xsl:value-of select="@statno" />
				</xsl:if>
			</h3>
			<xsl:choose>
				<xsl:when test='count(./*) > 0'>
					<table>
					<tr><th>Name</th><th>Value</th></tr>
					<xsl:for-each select="./*">
					<tr>
						<td><xsl:value-of select="@name" /></td>
						<td><xsl:apply-templates select="." /></td>
					</tr><xsl:text>
					</xsl:text>
					</xsl:for-each>
					</table>
				</xsl:when>
				<xsl:otherwise>
					<i>None</i>
					<br/>
				</xsl:otherwise>
			</xsl:choose>

		
		</xsl:for-each>
		</div>
	</xsl:template>

	<xsl:template match="libraries">
		<xsl:call-template name="menulist"/>
		<div><xsl:call-template name="startdiv"/>
		
		<xsl:for-each select="library">
			<h3><xsl:value-of select="@name" /> @ <xsl:value-of select="@file" /></h3>
			<xsl:choose>
				<xsl:when test='count(./*) > 0'>
					<table>
					<tr><th>Name</th><th>Value</th></tr>
					<xsl:for-each select="./*">
					<tr>
						<td><xsl:value-of select="@name" /></td>
						<td><xsl:apply-templates select="." /></td>
					</tr><xsl:text>
					</xsl:text>
					</xsl:for-each>
					</table>
				</xsl:when>
				<xsl:otherwise>
					<i>None</i>
					<br/>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:for-each>
		
		</div>
	</xsl:template>

	<xsl:template match="screen|stack|dt|exception">
		<xsl:call-template name="menulist"/>
		<div><xsl:call-template name="startdiv"/>
		<pre>
		<xsl:choose>
		<xsl:when test='name()="screen"'>
			<xsl:for-each select="row">
				<xsl:value-of select="text()"/><xsl:text>&#x0A;</xsl:text>
			</xsl:for-each>
		</xsl:when>
		<xsl:otherwise>
			<xsl:value-of select="text()"/>
		</xsl:otherwise>
		</xsl:choose>
		</pre>
		</div>
	</xsl:template>

	<xsl:template match="variables">
		<xsl:call-template name="menulist"/>
		<div><xsl:call-template name="startdiv"/>
		<table>
		<tr><th>Regular expression filters for variables</th>
		<td><input type="text" id="txtName"/><button>
		<xsl:attribute name="onclick">FilterVars('div_<xsl:value-of select="name()"/>','idiv_<xsl:value-of select="name()"/>', document.getElementById('txtName').value)</xsl:attribute>Go!</button></td>
		<td>Matching is by regular expression so $ and . should be escaped e.g. \$. It is case insensitive and so typing <b>a</b> will match anything containing a or A.  Use blank for all.</td></tr>
		</table><br/>
		<div>
		<xsl:attribute name="onclick">HideDiv('div_<xsl:value-of select="name()"/>')</xsl:attribute>
		<xsl:attribute name="id">idiv_<xsl:value-of select="name()"/></xsl:attribute>
		<table>
		<thead>
		<tr><th>Type</th><th>Name</th><th>Value</th></tr>
		</thead>
		<tbody id='vars'>
		</tbody>
		</table>
		</div>
		</div>
	</xsl:template>

	<!-- call this for the clickable menu -->
	<xsl:template name="menulist">
		<li><span>
		<xsl:attribute name="onmouseover">style.color="red"</xsl:attribute>
		<xsl:attribute name="onmouseout">style.color=""</xsl:attribute>
		<xsl:choose>
		<xsl:when test='name()="variables"'>
			<xsl:attribute name="onclick">
				ToggleVars('div_<xsl:value-of select="name()"/>', 'idiv_<xsl:value-of select="name()"/>', null)
			</xsl:attribute>
		</xsl:when>
		<xsl:otherwise>
			<xsl:attribute name="onclick">
				ToggleDiv('div_<xsl:value-of select="name()"/>')
			</xsl:attribute>
		</xsl:otherwise>
		</xsl:choose>
		<u><xsl:value-of select="@name"/></u>
		</span></li><xsl:text>
		</xsl:text>
	</xsl:template>

	<!-- add attributes for the opening DIV -->
	<xsl:template name="startdiv">
		<xsl:attribute name="id">div_<xsl:value-of select="name()"/></xsl:attribute>
		<xsl:if test='name()!="variables"'>
			<xsl:attribute name="onclick">style.display="none"</xsl:attribute>
		</xsl:if>
		<xsl:attribute name="style">display: none;</xsl:attribute>
	</xsl:template>

	<!-- use this for a suitable title -->
	<xsl:template name="title">
		Panic analysis: <xsl:value-of select="//basics/filename"/>
	</xsl:template>
	<!-- protect against ticks at start of fn names in var section -->
	<xsl:template name="fmtname">"<xsl:value-of select='@name'/>"</xsl:template>
</xsl:stylesheet>

