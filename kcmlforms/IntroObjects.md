Objects

Forms are one example of a KCML object. An object is a self-contained entity which contains all of the information about its activities and state within itself. Objects can contain other objects in an hierarchical fashion. Objects have **properties** that can be set or inspected in the KCML program and they often have functions called **methods** associated with them that allow the KCML program to control their behaviour. Objects, in particular objects that interact with the user, can raise **events** which cause KCML code to be executed in response in a subroutine called an **event handler**.

KCML5 introduces a new dot notation to reference the properties or call the methods of an object. For instance a.b.c() represents making a method call c() into the object b which itself is part of the object a.
