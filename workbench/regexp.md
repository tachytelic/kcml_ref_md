## Regular expressions

Each statement is considered to be a line. Thus the pattern ^STR finds all the statements that start with a STR() function.

|  |  |
|----|----|
| c | The character c where c is not a *special character* |
| \c | The character c where c is any character except a digit 1 to 9 |
| ^ | The beginning of the line |
| \$ | The end of the line |
| \[s\] | Any character in the set s where s is either a list of single chararacters e.g. \[abcABC\] or a range separated with a - e.g. \[a-c\] or some combination |
| \[^s\] | Any character not in the set s. |
| . | matches any character |
| r\* | matches zero or more occurrances of the regular expression r with the longest leftmost match chosen |

Searches with a type of *Symbols Only* do not use regular expressions but use ? and \* to match a single wild character or many wild characters respectively.
