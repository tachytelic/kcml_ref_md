LIST M

------------------------------------------------------------------------

<div class="Generalform">

General Form:

<div class="indent">

LIST \[title\] M

</div>

Where:

<div class="indent">

title = alpha_variable or a literal string

</div>

</div>

------------------------------------------------------------------------

The LIST M statement lists loaded libraries and selected globals showing for each one its name and the memory mapped file it was loaded from. In the case of a process global it will show the partition number of the partition owning the shared memory. The order of the list is the order of loading with the earliest one at the top.

See also:

[LIBRARY ADD](MODULE.htm), [SELECT @PART](SELECT_@PART.htm)
