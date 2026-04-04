Language numbers

KCML has a convention for numberering supported languages. It was originally devised for use in byte 20 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE20) to specify the language for the chevron notation used for [internationalized strings](TutorialLangs.htm) but it is optional in that context and many applications prefer to use their own numbering scheme.

The language number can be set into byte 61 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE61) to specify the code page to use when converting between UTF-8 and a code page using the E="UTF-8" extended form of [\$PACK]($PACK.htm). This byte should be set to HEX(FF) if the server is running in Unicode mode, i.e. with the environment variable [USING_UTF8](EnvVars.htm#USING_UTF8) set, as the UTF-8 pack format will just become a copy.

It is also used in [\$MACHINE]($MACHINE.htm#BYTE33) byte 33 to indirectly indicate the kclient's user locale in Microsoft Windows. The client arrives at the language code by starting with the locale. Some locales are split e.g. UK English and US English and such split locales will have a default for all the locales that are not explicitly checked. Thus for English the locale is defaulted to be US English unless specifically identified as UK English. In the case of Chinese the exceptions are HongKong and Taiwan which are presumed to be Traditional. All other Chinese locales (PRC, Singapore) are assumed to be Modern.

Note that the client will only check the PC locale when it starts up and if the user's locale is changed in the Windows Control Panel while the client is running, neither the client nor the server will be aware of the change.

Language codes 17 to 20 were added to KCML 6.20+ after build 13326.
