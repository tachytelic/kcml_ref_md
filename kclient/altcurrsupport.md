# <span id="alternatecurrencysupport"></span> Alternate currency support

Kclient supports a simple dual currency mode whereby currency fields on forms can be switched by the kclient between currencies using a rate specified in the KCML server program by the [\$CONVERT](mk:@MSITStore:kcmlrefman.chm::/$CONVERT.htm) function. If this function has set a rate then a currency button will appear on the title bar of any form that displays controls containing currency values. These controls will have been typed by the program as appropriate for this purpose. By toggling the title bar button the client can switch between the two currencies.

This dual current switch is only enabled if the checkbox on this property page is set on. To distinguish such currency fields colors can be chosen for read-only and editable states of currency fields when displaying the alternate currency.

While this feature is intended for use as in Europe within the countries of the EMU, it has more general application in other countries where two currencies circulate. Clearly this technique is no substitute for multicurrency accounting.

<div id="ClickDiv">

<u>Click here to view an example dialog</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example dialog</u>

## <img src="bitmaps/europref.gif" data-border="0" alt="Euro currency dialog" />

</div>
