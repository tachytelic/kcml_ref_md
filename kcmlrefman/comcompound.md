### <span id="Compound">Compound object references</span>

Where a hierarchy of objects exists it is not necessary to extract each object reference separately so the following expression

OBJECT b = a.List() OBJECT c = b.Next()

could be shortened to

OBJECT c = a.List.Next()

These expressions can be of arbitrary length.

OBJECT a = A.B.C(10,20).D(1).E("hello")

However there is a performance penalty associated with evaluating such expressions and generally if you need to access an object repeatedly it is better to get direct object reference rather than refer to it through a complex expression. Thus FOR OBJECT ww IN worksheet.Range("A14:F18") OBJECT font = ww.font font.colorindex = i++ font.Bold = TRUE NEXT OBJECT ww is, in this case marginally, better than FOR OBJECT ww IN worksheet.Range("A14:F18") ww.Font.colorindex = i++ ww.Font.Bold = TRUE NEXT OBJECT ww
