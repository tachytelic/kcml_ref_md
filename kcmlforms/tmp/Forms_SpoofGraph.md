SpoofGraph method

<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> SpoofGraph(Spoof)

The SpoofGraph() method controls the spoofing of graphs. The spoofing of graph involves spotting the use of the Bits Per Second (Pinnacle) Graph Server OCX and using the standard built in [Graph control](/IntroGraph.htm) of kclient instead. A small number of properties are also supported. If the Graph Server OCX is not installed then spoofing is automatic. The Graph control was designed to replace the Graph Server OCX where the OCX was not available (for example CE based terminals) or not installed; spoofing is enabled by default to give a common look and feel across all platforms. However, applications may need or rely on the much greater functionality of the Graph Server OCX or prefer the 3D and other graph styles, and this method allows the application to override the default behaviour. This method need only be used once within an application to control all graph use.

The following example disables graph spoofing: REM Get KClient control object OBJECT client = CREATE "ClientCOM", "KClient" REM Get Forms control object OBJECT forms = client.GetForms() REM Disable automatic spoof of graph forms.SpoofGraph(FALSE)

##### See also:

[PersistFormSize](/tmp/Forms_PersistFormSize.htm), [SetToolBarSize](/tmp/Forms_SetToolBarSize.htm), [TabEnterKey](/tmp/Forms_TabEnterKey.htm), [TabReturnKey](/tmp/Forms_TabReturnKey.htm), [UserColor](/tmp/Forms_UserColor.htm)
