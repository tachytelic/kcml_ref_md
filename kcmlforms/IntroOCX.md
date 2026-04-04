OCX control overview

An **OCX** is a component object which can come from a number of sources including Microsoft and third part software vendors. They are a special type of COM object which is designed to be embedded within a container object. A Kclient form acts as a container and can instantiate any OCXs that meet the Microsoft OCX96 specification. They can enhance forms in powerful ways but they have the drawback that they must be specially installed on any PC the needs them. This is contrary to the modern concept of the thin client.

An **ActiveX** control is a subset of the more general OCX specification and can be considered as an OCX for our purposes.

To use an OCX on a KCML form you must first embed it on the form at design time using the Forms Designer. This is described in the section on [Working with OCX Controls](FormsDesignerWorkingWithOCXControls.htm). The form definition will contain a skeleton definition of the OCX specifying the container properties such as size and placement as well as the ProgId that uniquely identifies the control. If the form is sent to a PC client that does not have that OCX installed then the container are will appear blank with the ProgId in text.

The forms designer does not directly support setting OCX properties at design time though some OCXs have a design mode that allows properties to be set by internal dialogs contained in the object. This is generally invoked by right clicking the OCX in the forms designer. You can set the container properties however.

The OCX is instantiated when the form is sent to the client, i.e. between the [.Enter()](tmp/PROP_FORM_ENTER.htm) and [.Show()](tmp/PROP_FORM_SHOW.htm) events. This means that you must not attempt to manipulate the OCX within any Create() or .Enter() event handler as the object will not have been created. Instead you should add code to the .Show() event to get an OBJECT reference for the OCX that can be used to set properties and call methods. Similarly you cannot reference an OCX object in the [.Exit()](tmp/PROP_FORM_EXIT.htm) handler as the object will have been shutdown before this event is triggered.

LOCAL DIM OBJECT c DEFEVENT Form1.form.Show() OBJECT c = .ocxControl1 c.Random = TRUE c.Draw() END EVENT

Note that the object variable is declared as a local variable within the form. This ensures that the object reference is properly released when the form is closed.

OCXs usually trigger events which can be handled with event handlers in the usual way.

Compatibility issues

In KCML 5.02 and earlier versions of KCML 5 there was support for a limited subset of OCX controls conforming to the original pre-OCX96 specification. The full specification of the control was extracted from its type library by the Forms Editor and was saved inside the form definition. The encoding scheme did not handle controls with a hierarchy of component objects nor did it handle OCX96 spec property methods.

KCML 5.03 implements the full OCX96 specification by treating OCXs like any other COM object except that the forms Open() method will automatically instantiate it within the form container. It will not be necessary for the form to contain a specification of the properties and methods available as this can be discovered by KCML at runtime. Old forms will be accepted by the new KCML 5.03 forms designer though this information will be ignored if the OCX controls are accessed as objects. New forms created with the KCML 5.03 forms designer will not contain these property and method specifications which for some controls will be a significant space saving

Other issues

Using an OCX, or indeed any COM object, in your application breaks the rules for a thin client as you cannot always be certain that the OCX will be available on the client. If it is not present then you will have to deploy the OCX on every client which presents a real problem in organizing this and in managing versions. To a certain extent you can rely on core Windows objects such as the HTML browser control always being there (though it may not be on some CE clients).

You should think very carefully before relying on an OCX in your application.
