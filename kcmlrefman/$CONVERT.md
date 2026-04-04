\$CONVERT

------------------------------------------------------------------------

\
General Forms :\
\
1.      \$CONVERT = alpha_expression\
\
2.      alpha_receiver = \$CONVERT\
\

------------------------------------------------------------------------

This function is used to alter the display and input of currency values by specifying an alternative currency name and exchange rate, or to specify a scaling factor for currencies that need very high numeric values.

Using \$CONVERT to specify an alternative currency

This function is used to specify two currency names and a conversion rate to convert between them. The specified rate is then used with [PRINTUSING](PRINTUSING.htm) to allow reports to dynamically switch the value of currency fields. It is also used by multi-currency enabled forms to automatically convert form fields between two currencies. The native currency can be converted to the alternative currency by either dividing by or multiplying by the rate. The default is to divide.

The alpha expression should specify three to five comma separated fields. The first two fields indicate the labels to be used on the KCLient title bar if multi currency forms are being used. The third field defines the actual exchange rate to be used. At least three fields must be present and spaces are ignored. The fourth field specified the number of digits after the decimal for rounding (0 to 4) and is optional. The last field is either a '\*' or '/' indicating whether the native currency should be multiplied or divided by the rate to calculate the alternative currency. This field is optional and defaults to '/'. The string cannot exceed 64 characters though only the first 3 characters of the labels will be used. As the rate may be used to divide in the convertion, it must be non-zero. For example:

\$CONVERT="GBP,EUR,0.62"\
\$CONVERT="EUR,GBP,1.61,2,\*"

Currency fields are defined in [PRINTUSING](PRINTUSING.htm) images by the use of the dollar (\$) sign instead of the hash (#) symbol. However, to enable this feature you must set the HEX(10) bit of [\$OPTIONS RUN]($OPTIONS_RUN.htm) and change the default leading currency symbol specified in byte 4 of [\$OPTIONS]($OPTIONS.htm#BYTE4) to a hash symbol, e.g. STR(\$OPTIONS,4 ,1) = "#". For example:

STR(\$OPTIONS, 4, 1) = "#"\
STR(\$OPTIONS RUN, 47, 1) = OR HEX(10)\
\$CONVERT = "GBP, EUR, 0.62"\
PRINTUSING "-\$\$\$\$\$.\$\$ -#####.##", 5, 5

would give the following output:

 8.06 5.00

If \$CONVERT is set then KClient will enable the title bar button on forms allowing the user to switch the display of currency values in edit controls and grid control cells between the two currencies (CTRL+E can also be used to switch between currencies). For greater visual impact, the KClient preferences dialog has an "Alternative Currency" tab allowing the user to choose a different color for all fields displayed in the alternative currency.

If the currency value in a edit control or grid cell is switched to the alternative currency and then edited, the client will need to convert back to the main currency and this may involve rounding. The number of digits to round is settable with the optional fourth field. If not set the client will use its own knowledge of the currency settings for the locale as supplied by Windows.

Currency fields to be converted must be edit control or grid control cells that have a numeric type and have the CanConvert property set to TRUE. The HEX(20) bit in byte 47 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE47) reflects the currently selected currency. This bit is set when the client connects to the server, and is updated when the client changes the current currency.

This statement can also be used as a function returning the current \$CONVERT value, e.g.

CurrencyInfo\$ = \$CONVERT

Using \$CONVERT to specify a scaling rate

This form of \$CONVERT was introduced in KCML 6.10. It is based on the same principles as the first form, int that it affects edit controls and grid cells that have numeric type and the CanConvert property set. However, it does not present the user with an alternative display, but instead displays all values by \$CONVERT scale specified by appending zeros to the output. These zeros are stripped on input. To scale all values by 1,000 the \$CONVERT string should be set to "000".

Note:

\$CONVERT was first implemented in KCML 5.02. Support for the optional fourth and fifth fields was introduced with KCML 6.0. The scaling form was introduced in KCML 6.10.

See also:

[\$OPTIONS]($OPTIONS.htm), [\$OPTIONS RUN]($OPTIONS_RUN.htm), [PRINTUSING](PRINTUSING.htm)
