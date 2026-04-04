Date functions supported

KISAM does not have a data type for TIME data or for time stamps so only DATE functions are available.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>CURDATE( )</td>
<td>Returns the current date as a date value.</td>
</tr>
<tr>
<td>DAYNAME(<em>date_exp</em>)</td>
<td>Returns a character string containing the name of the day (for example, Sunday).</td>
</tr>
<tr>
<td>DAYOFMONTH(<em>date_exp</em>)</td>
<td>Returns the day of the month in <em>date_exp</em> as an integer value in the range of 1-31.</td>
</tr>
<tr>
<td>DAYOFWEEK(<em>date_exp</em>)</td>
<td>Returns the day to the week in <em>date_exp</em> as an integer value in the range of 1-7, where 1 represents Sunday.</td>
</tr>
<tr>
<td>DAYOFYEAR(<em>date_exp</em>)</td>
<td>Returns the day of the year in <em>date_exp</em> as an integer value in the range of 1-366.</td>
</tr>
<tr>
<td>MONTH(<em>date_exp</em>)</td>
<td>Returns the month in <em>date_exp</em> as an integer value in the range of 1-12.</td>
</tr>
<tr>
<td>MONTHNAME(<em>date_exp</em>)</td>
<td>Returns a character string containing the name of the month (for example January)</td>
</tr>
<tr>
<td>NOW( )</td>
<td>Returns current date and time as a timestamp value.</td>
</tr>
<tr>
<td>QUARTER(<em>date_exp</em>)</td>
<td>Returns the quarter in <em>date_exp</em> as an integer value in the range of 1- 4, where 1 represents January 1 through March 31.</td>
</tr>
<tr>
<td>TIMESTAMPADD(<em>interval</em>, <em>integer_exp</em>, <em>timestamp_exp</em>)</td>
<td>Returns the timestamp calculated by adding <em>integer_exp</em> intervals of type <em>interval</em> to <em>timestamp_exp</em>. Valid values of <em>interval</em> are the following keywords:<br />
SQL_TSI_DAY<br />
SQL_TSI_WEEK<br />
SQL_TSI_MONTH<br />
SQL_TSI_QUARTER<br />
SQL_TSI_YEAR</td>
</tr>
<tr>
<td>TIMESTAMPDIFF(<em>interval</em>, <em>timestamp_exp1</em>, <em>timestamp_exp2</em>)</td>
<td>Returns the integer number of intervals of type <em>interval</em> by which <em>timestamp_exp2</em> is greater than <em>timestamp_exp1</em>. Valid values of <em>interval</em> are the following keywords: SQL_TSI_DAY<br />
SQL_TSI_WEEK<br />
SQL_TSI_MONTH<br />
SQL_TSI_QUARTER<br />
SQL_TSI_YEAR</td>
</tr>
<tr>
<td>WEEK(<em>date_exp</em>)</td>
<td>Returns the week of the year in <em>date_exp</em> as an integer value in the range of 1-53.</td>
</tr>
<tr>
<td>YEAR(<em>date_exp</em>)</td>
<td>Returns the year in <em>date_exp</em> as an integer value.</td>
</tr>
</tbody>
</table>
