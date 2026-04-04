kverify utility

kverify \[switches\] file \[file \[...\]\]

This utility will verify the integrity of the indices of the specified tables, stopping if any problems are found. It can also be used to list table properties to stdout.

Five verification levels are supported.

1.  Only the controls are checked for a super-quick verification.
2.  As well as checking the controls, the sequence set of each index is checked to be in sequence and the free chains are followed to account for all blocks in the table.
3.  A more thorough verification which as well as doing a level 2 check, also checks that all the keys in the data area can be looked up in the index.
4.  For each rowid referenced in an index sequence set, the row is loaded and check to contain the right key segments. This can be slow on a large table and will catch only suble corruptions.
5.  This is like level 3 but the rowid of the data row must be found in a list of duplicates. This is a more exaustive test than level three but can be extremely slow on big tables with long runs of duplicates. If there are no indices with duplicates allowed then this is identical to level 3.

If the level is not explicitly specified with the -1 switch, then a level 3 verification is performed. For more infomation about higher levels and the tests performed see the [KI_VERIFY](tmp/KI_VERIFY.htm) function.

The following command line switches are supported:

| Switch    | Purpose                                              |
|-----------|------------------------------------------------------|
| -c        | print W user count only                              |
| -d        | print table properties only                          |
| -e        | print extent table only                              |
| -l        | verification level                                   |
| -p partno | specify 'partition' number to use when locking table |
| -r        | Open in mode R, default is X                         |
| -s        | silent mode. No messages printed.                    |
| -u        | open in mode U                                       |
| -v        | print version number only                            |

If a partition number is not specified, then a unique partition number is automatically allocated using the normal KCML rules for allocating background partition numbers.
