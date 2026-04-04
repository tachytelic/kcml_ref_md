Compatibility issues with the Graph Control

------------------------------------------------------------------------

The KCML Graph Control was added for KCML 5.03 and enhanced for KCML 6.00. It was designed to be a useful subset of the more sophisticated Pinnacle BPS Graph Server OCX which was the preferred graphing solution for previous version of KCML5. Despite having reduced functionality, the intrinsic control has some advantages over the OCX

- Startup time is faster. The OCX needs to start an EXE.
- The OCX must be separately installed and registered. This is not comptible with a thin client philosophy.
- While the runtime OCX is royalty free, a licenced SDK is required to program with this OCX.
- The OCX is not supported on Windows CE

The KCML client will spot the GraphServer OCX on a form and attempt to render the graph itself. To do this it can only use runtime set properties and methods as the design time property set is not available.
