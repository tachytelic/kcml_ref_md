## Tooltips

The editor and debugger support extensive tool tipping whereby a little yellow transitory window opens up next to a sensitive item if the mouse cursor is allowed to linger over that item. What it displays depends on the item

- Typically if held over a variable KCML will evaluate it and display its dimensioning information in the manner of [LIST DIM](mk:@MSITStore:kcmlrefman.chm::/LIST_DIM.htm). It can also evaluate expressions starting with [STR(](mk:@MSITStore:kcmlrefman.chm::/STR(.htm) or [FLD(](mk:@MSITStore:kcmlrefman.chm::/FLD(.htm).
- If used with a subroutine it will display the definition of the routine including the arguments. Furthermore if the [DEFSUB](mk:@MSITStore:kcmlrefman.chm::/DEFSUB.htm) line is followed by any [REM](mk:@MSITStore:kcmlrefman.chm::/REM.htm) comments then they will also be included. See [example](#subroutinetip) below.
- Tooltips for COM object methods will display the definition of the method taken from the type library

The toolbar is also tooltipped.

<span id="subroutinetip"></span>

<div id="ClickDiv">

<u>Click here for an example of a tooltipped subroutine reference</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example</u>

##### Example of subroutine tooltip

<img src="bitmaps/tooltipexample.png" data-border="0" width="605" height="135" alt="Tooltip referencing a subroutine" />

</div>
