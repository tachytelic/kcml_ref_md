Alternative Currency support

------------------------------------------------------------------------

For International applications developers, special support has been added to make it easy for forms to automatically convert between their native currency and an alternative currency and vice verse. The conversion is only performed within the KCML Edit and Grid Controls. To allow conversions to take place the Edit Control and Grid control cells must have the [Type\$](tmp/PROPSTR_TYPE.htm) property set to a numeric type (either N or I) and have the [CanConvert](tmp/PROP_KCMLEDIT_CANCONVERT.htm) property set to *TRUE*.

<span id="Setting_the_default_conversion_currencies_and_rates" setting_the_default_conversion_currencies_and_rates=""></span>Setting the default conversion currencies and rates

The [\$CONVERT](mk:@MSITStore:kcmlrefman.chm::/$CONVERT.htm) function is used to specify two currency names and a conversion rate to convert between them, for example:

\$CONVERT = "GBP, EUR, 6.543"

The currency name is placed on the forms title bar to show which currency is presently being displayed. The description held within the title bar is used to switch between the currencies, once clicked the controls that allow currency conversions will then. The specified value is used as the conversion rate.

<span id="_Enabling_alternative_currency_conversion_on_forms" _enabling_alternative_currency_conversion_on_forms=""></span><span id="Enabling_Euro_currency_conversion_on_forms" enabling_euro_currency_conversion_on_forms=""></span>Enabling alternative currency conversion on forms

To enable aternative currency conversions on forms you must set the HEX(20) bit in byte 47 of \$OPTIONS RUN, i.e.

STR(\$OPTIONS RUN,47,1) = OR HEX(20)

The KClient preferences must also be configured to allow currency conversions to take place. This is done by selecting the "Preferences ..." option from within the forms System Menu. Once in the preferences option, select the "Currency" Tab and check the option "Enable alternative currency mode". This option also allows you to change the default colors uses by convertable fields.

<span id="__Creating_forms_with_alternative_currency_support" __creating_forms_with_alternative_currency_support=""></span><span id="_Creating_forms_with_Alternative_currency_support" _creating_forms_with_alternative_currency_support=""></span><span id="Creating_forms_with_Euro_currency_support" creating_forms_with_euro_currency_support=""></span>Creating forms with alternative currency support

Only Edit controls and Grid control cells that have the [CanConvert](tmp/PROP_KCMLEDIT_CANCONVERT.htm) property set are able to switch between currencies. The Edit controls and grid cells must have the [Type\$](tmp/PROPSTR_TYPE.htm) property set in an appropriate way in order to represent the newly converted data

This rate is used by [PRINTUSING](mk:@MSITStore:kcmlrefman.chm::/PRINTUSING.htm) allow reports to dynamically switch the value of currency fields depending on the state of the HEX(10) bit in byte 47 of [\$OPTIONS RUN](mk:@MSITStore:kcmlrefman.chm::/$OPTIONS_RUN.htm). Currency fields are defined in [PRINTUSING](mk:@MSITStore:kcmlrefman.chm::/PRINTUSING.htm) by using \$ characters rather than the conventional \#. This means that the use of \$ as a leading currency symbol must be disabled by setting STR(\$OPTIONS,4,1) = "#".

Furthermore if [\$CONVERT](mk:@MSITStore:kcmlrefman.chm::/$CONVERT.htm) is set to non-blank then KClient will enable a titlebar button allowing the user to switch the display of currency values in Edit controls between the two currencies. You can also toggle by pressing CTRL-E in an edit control. Currency fields to be converted must be Edit controls which have a numeric [Type\$](tmp/PROPSTR_TYPE.htm) and which have the [CanConvert](tmp/PROP_KCMLEDIT_CANCONVERT.htm) property set to TRUE. The HEX(20) bit should be set in STR(\$OPTIONS RUN,47,1) to enable this feature. When toggled from the actual currency into Alternative Currency mode then the background of the Edit control will be switched to a color defined in the KClient form window preferences. It is possible to edit in this mode and KClient will convert figures edited this way back into the native currency when sending the data back to the KCML server.

The toggling of currency fields will be performed automatically by the client without further recourse to the server. However it is also possible to raise a [CurrencyChange()](tmp/PROP_FORM_EUROCHANGE.htm) event to customize this.

[\$CONVERT](mk:@MSITStore:kcmlrefman.chm::/$CONVERT.htm) can be used anywhere as a string expression returning the current value of the currency conversion settings. It is set by using it on the right hand side of a LET statement e.g

AltCurrency\$ = \$CONVERT
