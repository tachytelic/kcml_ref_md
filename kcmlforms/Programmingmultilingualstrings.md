Programming multi-lingual strings

------------------------------------------------------------------------

KCML allows multi-lingual strings to be used within programs. Each string is specified within Chevrons and byte 20 of the [\$OPTIONS RUN](OPTIONSRUN.htm) system variable is used to select the required string. For example, the following would assign the second string to the variable *Color\$*:

STR(\$OPTIONS RUN, 47,1) = HEX(02) Color\$ = \<\<"Red", "Rot", "Rouge"\>\>

When designing new forms it is possible to assign multiple string values to each text field. This is done by first adding a new language to the form, with the [Add New Language](TheLanguageMenuAddLanguageOption.htm) button in the forms designer. You can then select the required language and change any text fields required by the form. The language selected in the forms designer corresponds to the value set in byte 20 of \$OPTIONS RUN.

Text information for most controls on a form is almost always stored in the [*Text\$* property. To modify the](tmp/PROPSTR_TITLE.htm)

*Text\$* property within the program the Chevron syntax can be used in the normal way, for example:

.txtControl1.text\$ = \<\<"One, Two, Three", "Eine, Zwei, Drei", "Une, Deux, Trois"\>\>
