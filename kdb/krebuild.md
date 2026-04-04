krebuild utility

This utility rebuilds a tables index directly from the data. This is faster than dropping exiting indices and creating new ones in SQL.

Unless the optional -f switch is specified, then a fast rebuild will be attempted using the existing sequence set and just rebuilding the index set to compact index block and optimally balance the index tree. This is a lot quicker than a full rebuild, as the data rows will not be examined. However, if the index is found to be inconsistent during a fast rebuild, then a full rebuild will be automatically performed. Full rebuilds will rebuild the free data chain.

This utility can reformat the index to a more modern [index format](legacy_types.htm). Unless the -4 switch is specified, then version 3.0 tables will be rebuilt as version 3 and version 4 tables will be rebuilt as version 4. With this switch, version 3.0 tables will be converted to version 4 tables. Similarly earlier versions can be converted to type 6 with the -6 switch. To convert tables to type 7 the [kconvert](kconvert.htm) utility must be used.

| Switch    | Purpose                                              |
|-----------|------------------------------------------------------|
| -c        | consolidate extents                                  |
| -f        | full rebuild                                         |
| -p partno | specify 'partition' number to use when locking table |
| -s        | silent mode. No messages printed.                    |
| -u        | use access mode 'U' to open table                    |
| -v        | print version only                                   |
| -V level  | set verbose level                                    |
| -4        | rebuild as type 4 index                              |
| -6        | rebuild as type 6 index                              |

If a partition number is not specified, then a unique partition number is automatically allocated using the normal KCML rules for allocating background partition numbers.

A significant amount of temporary work space of as much as twice the index size is required and this needs to be available in the systems temporary directory however the environment variable *WORKSPACE* determines where temporary work files are created and can be used to redirect work files to a bigger filesystem.
