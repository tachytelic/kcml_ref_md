KCML Statements and commands

------------------------------------------------------------------------

1.1 Introduction

1.1.1 KCML Statements and Commands page layout

This section contains a complete list of **KCML** statements, commands, functions and operators in alphabetical order. In general this section assumes that Unix is the operating system being used. Unless specified, all statements and commands are implemented in the same way for the DOS and Windows versions. Each instruction is laid out as follows:

Instruction title

The instruction name and type are printed on the first line of the page. The types of instructions found in this section are *functions*, *statements*, *commands* and *operators*.

A *function* is used as part of a numeric or alphanumeric expression within a *statement*. Functions have a left parentheses printed immediately after the function name. If the function does not require an open parentheses after the function name, the word \`function' is printed after the function name.

A *statement* is a programmable instruction. A *command* is a non-programmable instruction entered in immediate mode. Instructions that can be entered as statements and immediate mode commands have no instruction type printed on the instruction title line. Instructions that can only be entered in immediate mode have the word \`command' printed next to the instruction name.

An *operator* is used to perform operations on alpha-operands. Operators have the word \`operator' printed next to the instruction name.

General Form

The general form box describes the usage of the instruction. The conventions used are as follows:

- Uppercase letters (A-Z) represent the instruction, or part of the instruction. Some instructions include other special characters, including \`\$', \`#' or \`(' signs, such as the \$ALARM statement. Instructions must be entered as shown by the uppercase letters, without any spaces (unless specified), between characters.

- All lowercase words represent information that must be supplied.

- If braces are used to contain a vertical list within the format of an instruction, then one of the options must be selected from the list and used with the command. For example:

       <img src="bitmaps/volume2_intro.gif" data-align="BOTTOM" data-border="0" alt="volume2_intro.gif" />

  means that the LEN( function should be supplied with either an alpha variable or a field variable.

- If square brackets \`\[\]' are used to contain either a vertical list or a single description, indicates that the enclosed information is optional, i.e. you can use any one option or no option at all. For example:

       <img src="bitmaps/volume2_intro1.gif" data-align="BOTTOM" data-border="0" alt="volume2_intro1.gif" />

  means that the \$BREAK statement could be followed by either an \`!', a numeric expression \`num_expr', the keywords ON or OFF, or nothing.

- When ellipsis \`...' appear within the format, they indicate that the description immediately preceding can occur one or more times. For example:

       receiver_variable = ... ADD\[C\] alpha_operand ...

  means that the ADD operand may be used several times within the statement. The ellipsis can also mean, as in the example above, that other instructions may be used within the same statement.

Description

The description section of the instruction page describes the instruction, and discusses the usage of the instruction.

Examples

One or more programming examples are given, where possible. Some examples are working program segments, these are shown with the output after the RUN<span style="color: #00ff00; "> </span>command was executed.

Syntax examples

One or more syntax examples are given, where possible, for each instruction. Examples of syntax may also be used in the description section.

Compatibility notes

The compatibility notes refer to previous versions of **KCML**, or inconsistencies between the Unix, DOS and Windows versions.

See also

The See also section supplies references to other sections within the manual. Words in upper case are **KCML** statements and commands and can therefore be found in this volume. Words in lower case refer to **KCML** utility programs and can be found in Chapter 19 of Volume 1. Words in italics refer to environment variables and can be found in chapter 20 of Volume 1. Uppercase words followed by a single parentheses '(' refer to a function.

1.1.2 General Terminology

The following terms are widely used within this section of the manual:

|  |  |
|----|----|
| alpha_array | An alpha array variable must be used. |
| alpha_expression | An alpha expression must be used. This includes string functions and literals. Multi-language strings can also be specified |
| alpha_operand | An alpha variable, literal string, or string function, generally used by alpha operators. |
| alpha_receiver | A series of alpha variables or array variables, delimited by commas. Receivers can be modified. At least one alpha variable must be specified. |
| alpha_receiver_array | An alpha array variable used to receive the result of an alpha expression, usually associated with MAT statements. |
| alpha_variable | An alpha variable, FLD( or STR( function must be specified. Alpha variables may be scalar or array variables. |
| /devaddr | A **KCML** device address in the format /hhh where h is a hexadecimal digit in the range 0-9, A-F. |
| filename | The name of a **KCML** program or data file. The term, filename refers to both catalogued files and native Unix/Windows files. File names are generally up to 8 characters in length, this is a hangover of Wang BASIC-2. Native Unix/Windows files can have a file name length ranging from 1 to the maximum filename length supported by that operating system. |
| hex_digit | A hexadecimal digit in the range 0-9, A-F. |
| literal_string | An alpha literal string consisting of a string of characters enclosed in quotes or a hex literal, specified with the HEX( statement, must be specified. |
| line_number | A valid **KCML** line number must be specified. Line numbers can range from 0 through to 32000. |
| numeric_array | A numeric array variable must be specified. |
| numeric_expression | A numeric expression consisting of numeric constants, functions and variables, must be specified. |
| numeric_receiver | A numeric scalar or array element is used to receive the results of an expression or operation. |
| numeric_receiver_array | A numeric array used to receive the results of an expression, usually associated with MAT statements. |
| numeric_scalar | A valid numeric scalar variable must be specified. |
| numeric_variable | A valid numeric scalar or array variable must be specified. |
| platter_image | Refers to a **KCML** platter image file, containing a catalogue index and a number of program or data files. Support for platter images is maintained for compatibility reasons only. |
| \#stream | A valid **KCML** stream number in the format \#nnn where n is a numeric expression in the range 0 <u>\<</u> 255. |
| nativefile | An individual Unix/Windows file, not necessarily created by **KCML**. |
