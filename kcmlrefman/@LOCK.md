@LOCK

------------------------------------------------------------------------

General Form:\

@LOCK

------------------------------------------------------------------------

This statement implements advisory locking of the currently [SELECTed](SELECT_@PART.htm) global partition. Advisory locking means that after an @LOCK other partitions can still read or write the global variables but if they issue an @LOCK themselves they will sleep until the global is unlocked with the [@UNLOCK](@UNLOCK.htm) statement. If no global has been selected then these statements have no effect.

Only implemented for process globals and not for memory mapped globals.

Example:

@LOCK\
IF @lock_flag = 0 THEN @lock_flag = \#PART\
@UNLOCK

See also:

[@UNLOCK](@UNLOCK.htm)
