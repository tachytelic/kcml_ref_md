Wang 2x36 series

(KTERM=wang or KTERM=w2236)

The Wang 2536 terminal has optional XON/XOFF flow control and can be connected to any UNIX CPU but 2x36 terminals previous to the 2536 can only use the 2200 proprietary flow control protocol. Flow control is a convention whereby a terminal can regulate the flow of characters to its screen or printer by sending special reserved characters to the CPU to stop and start the flow. The old Wang 2x36 terminal used four such characters but industry standard terminals use just two. Wang style flow control has been implemented by the manufacturer on some UNIX machines specifically to support **KCML** (e.g. Altos 1000, CCI6/32, ICL DRS500) and it is also available on 386/486 PCs using either Chase Research or DigiBoard AT/EISA bus terminal controllers. However in general these older Wang terminals can only be connected to a UNIX CPU through an external protocol converter like a Kerridge Z-net or through a Chase Research IOLAN terminal server using Ethernet.

If the manufacturer does not directly support Wang flow control, function keys 17 and 19 will not work correctly as they send characters which conflict with XON/XOFF flow control. Pressing SF19 will stop the computer transmitting and SF17 will restart it. **KCML** will not see either key.

These terminals have a very straightforward *TERMINFO* description as the terminal responds directly to **KCML** command sequences and most keys can be sent directly. Local printing is supported but if the printer is off-line then the screen will also be off-lined.

Character set

These terminals use a proprietary 7 bit character set. The standard terminal has a font which displayed many Latin characters but there were variants for Germany, Switzerland etc. The US character set

<div id="ClickDiv">

<u>Click here to view the US 2x36DW character set</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the dialog</u>

<img src="bitmaps/charsetdw.png" data-border="0" alt="2x36 US character set" />

</div>

To use this terminal in a non-English locale with KCML5 which requires Latin-1 you will need to add some mapping entries to [TERMINFO](TextTermKybMap.htm) e.g. \# 7 bit international characters from standard US terminal \# mapped back to Latin-1 characters \# These may be ambiguous with editing keys like ^A and ^V map('Â')=\x00 map('Ê')=\x01 map('Î')=\x02 map('Ô')=\x03 map('Û')=\x04 map('À')=\x05 map('È')=\x06 map('Ù')=\x07 map('É')=\x08 map('á')=\x0F map('â')=\x10 map('ê')=\x11 map('î')=\x12 map('ô')=\x13 map('û')=\x14 map('ä')=\x15 map('ë')=\x16 map('ï')=\x17 map('ö')=\x18 map('ü')=\x19 map('à')=\x1A map('è')=\x1B map('ù')=\x1C map('Ä')=\x1D map('Ö')=\x1E map('Ü')=\x1F map('é')=\x7D map('ç')=\x7E
