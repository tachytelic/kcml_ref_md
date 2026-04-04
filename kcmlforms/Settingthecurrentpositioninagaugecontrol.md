Setting the current position in a gauge control

------------------------------------------------------------------------

To set the current position in a gauge control the

*Position* property is used. For example, the following would set the position in the gauge control to 50%.

.gaugeControl1.Position = 50

and to retrieve the current setting from the control you could use the following:

CurPos = .gaugeControl1.Position

<span style="font-family: Courier New,monospace; "> </span>Note that if you are changing the gauge position within an event handler that the position will not be updated until the event has completed. To continually update the gauge within an event handler you should call the

*Flush()* form method immediately after the gauge position is changed.
