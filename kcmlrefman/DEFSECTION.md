DEFSECTION

------------------------------------------------------------------------

<div class="Generalform">

General Form:

<div class="indent">

DEFSECTION sectionname\
   ...\
   ...\
END SECTION

</div>

\

</div>

------------------------------------------------------------------------

A DEFSECTION defines a logical section of a [library](TutorialModules.htm). This instruction is used for program presentation and structure and has no effect at runtime. It allows you to manage and group subroutines together so that the KCML Workbench function browser can then display functions using these section groupings. The DEFSECTION and END SECTION statements must always be balanced.

DEFSECTION has an effect only in a library though it can be used in any program.


    DEFSECTION section_1
            
        DEFSUB 'sub1_1()
        ...
        END SUB
            
        DEFSUB 'sub1_2()
        ...
        END SUB
            
    END SECTION

    DEFSECTION section_2
    ...
     ENDSECTION
