KCML language overview

What is KCML?

The **KCML** programming language is an incremental compiler. This means that each line of a program is compiled into an efficient internal form as the lines are entered. The internal form is then executed to run the program. **KCML** can later reconstruct the original line(s) to allow the program to be modified if necessary. This gives **KCML** the best features of a compiled and an interpreted language, and in particular it provides a high degree of portability.

The language is made up more than a hundred statements and functions that can be used within programs to write advanced powerful and efficient applications. Tasks that are often complex and laborious in other languages like sorting, string searches, matrix arithmetic, etc., can all be done quickly and efficiently with single **KCML** statements.

Runtime and development

**KCML** has no distinction between a runtime and a development version. When **KCML** is installed both are available, it is up to the developer to hide the development aspect of **KCML** from the user if required. Various functions of **KCML** including the development environment can be disabled and re-enabled by directly modifying switches within **KCML** programs.

Multi-user features

Regardless of the environment, **KCML** is a true multi-user language allowing users to share data, programs and peripheral devices. **KCML** maintains unique terminal numbering mechanism for each **KCML** process on the system. File and record locking is maintained automatically within the built in database. Statements are available to maintain locks on other files and devices external to the built in database. In client server configurations, programs can be written to allow business logic functions to be available to all **KCML** processes running on the server.

Compatibility and portability

In general, programs and data files written on any **KCML** supported platform can be used unchanged on any other **KCML** supported platform. It is perfectly possible to develop on a Windows 95 laptop and run the resulting program on a HP9000 server. Today **KCML** is available on all modern popular platforms including Microsoft NT, Microsoft Windows 95 and 98, IBM RS/6000 range running AIX, the Hewlett Packard HP9000 range running HP-UX, the Data General AViiON, Sun SPARC machines running Solaris, Compaq Alpha running Digital Unix, Tandem Unix servers and various Intel procesor machines running SCO Unixware. There are also ports of KCML4 for SCO Openserver, DOS and Windows 3.x

Compatibility with BASIC-2 and other BASIC-2 dialects

Since **KCML** was originally designed around the language used by the Wang 2200 a considerable amount of compatibility is still maintained with the original BASIC-2 and with some of the other dialects of that are available.

Development on the original BASIC-2 language has long since ceased, other dialects are still being developed. **KCML** is almost entirely compatible with all BASIC-2 releases up to and including the 3.4 version. It supports the global patition concept of the multiuser language. **KCML** has also maintained compatibility with the BASIC-2C dialect up to release 3.2. The BASIC-2C dialect is still being developed and is now known as NPL, but the languages in recent years have started to diversify and we therefore will not make any attempt to maintain compatibility with recent and future generations of this dialect.

Compatibility with previous versions of KCML

Tools are provided with **KCML** to assist developers who with to upgrade from older generations of **KCML** to the latest version. It has always been our commitment to ensure that all new versions are compatible with older versions.
