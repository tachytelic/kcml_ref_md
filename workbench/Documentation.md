## New documentation

The documentation for KCML 6.00 has been extensively revised and reworked in Microsoft Htmlhelp format. This is the new help format based on HTML that was introduced with Windows 98 and which is slowly replacing WinHelp for on line documentation. Even if you use NT or Windows 95R2, 98 or 2000, it is quite likely that if you have installed a recent MS product (e.g. IE4.01 or IE5) it will have installed the viewer already but if you have Windows 95 and cannot get help then it is available for download from [microsoft.com](http://msdn.microsoft.com/library/tools/htmlhelp/wkshp/hhupd.exe) (716kb). Note you must have IE4 or greater on your machine to use this (it need not be your default browser however).

Features

- Uses browser technology and can link directly to the Internet
- All help now merged into one help system with a common table of contents
- Much better integration with the Workbench
- F1 context help on KCML reserved words, functions and CALLs
- Indexed by keyword and also with general word search capability
- Favorites tab to bookmark entries

All the component help files are installed from the Developer Resources section of the [download area of the KCML web site](http://www.kcml.com/download).

You can add your own application help lookup for [DEFSUB](mk:@MSITStore:kcmlrefman.chm::/DEFSUBquote.htm)s by creating a help file and having the subroutine name (without the tick) in the index. Create a registry key called **ApplicationHelp** under HKEY_LOCAL_MACHINE/Software/Kerridge/Documentation. This should have two string values and one DWORD value

|  |  |
|----|----|
| Menu | The text to display in the workbench Help menu. Use an & character to set a keyboard shortcut |
| Path | The full pathname of the help file |
| Workbench | This DWORD value should be set to 1 to tell KCML that this particular entry applies to the workbench. Entries without this value will only appear in the old KCML5 editor help menu. |

The Workbench help system will recognize compiled HTML Help files with a .CHM extension and the original WinHelp format helpfiles with a .HLP extension and individual HTML files with a .HTM extension (though these last can't be indexed).
