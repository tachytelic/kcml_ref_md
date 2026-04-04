SOAP client examples

These examples use services published on the excellent [www.xmethods.com](http://www.xmethods.com) website. They specify a proxy server in the optional arguments to [CREATE](CREATE.htm#SOAP) which may not be necessary at your site and could be dropped.

Simple usage

This is a simple example that is passed two strings and returns a number.


    DIM rate, opt$="PROXY=proxy:8080"
    OBJECT s = CREATE "SOAP", "http://services.xmethods.net/soap/urn:xmethods-CurrencyExchange.wsdl", opt$
    rate = s.getRate("England", "Japan")
    OBJECT s = NULL

Returning a sequence

A sequence is a structure and if often used in SOAP methods to return multiple results from one call. It does not map onto any native KCML datatype so KCML unrolls the structure into its individual elements which must be passed BYREF from the method. According to its [WSDL](http://live.capescience.com/wsdl/AirportWeather.wsdl), the getSummary() method in the example only takes one input parameter and returns one sequence. The sequence will be unrolled into its 7 component elements which must be added to the call as BYREF or REDIM arguments. Nested sequences are not supported and all the elements from the sequence must be specified in the call.

<span id="weatherexample"></span>

In this example you can look up the [weather](http://www.capescience.com/webservices/airportweather/index.shtml) at an airport given its 4 character ICAO identifier. (e.g. Heathrow is EGLL, Los Angeles is KLAX. The nearest reporting aerodrome to Hungerford is EGVN.)


    DIM opt$="PROXY=proxy:8080"
    OBJECT s = CREATE "SOAP","http://live.capescience.com/wsdl/AirportWeather.wsdl",opt$
    ERROR DO
        END
    END DO
    frmWeather.Open()
    OBJECT s = NULL
    END

    - DEFFORM frmWeather()=\
         {.form,.form$,.Style=0x50c000c4,.Width=387,.Height=253,.Text$="METAR decoder",.Id=1024},\
         {.editControl1,.kcmldbedit$,.Style=0x50810080,.Left=165,.Top=22,.Width=135,.Height=13,.Id=1006,.EditGroup=.editgroup2,.Label$="ICAO code"},\
         {.editLocation,.kcmldbedit$,.Style=0x50810080,.Left=92,.Top=79,.Width=207,.Height=13,.Id=1002,.ReadOnly=1,.EditGroup=.editgroup1,.Label$="Location"},\
         {.editSky,.kcmldbedit$,.Style=0x50810080,.Left=92,.Top=110,.Width=207,.Height=13,.Id=1003,.ReadOnly=1,.EditGroup=.editgroup1,.Label$="Sky conditions"},\
         {.editWind,.kcmldbedit$,.Style=0x50810080,.Left=92,.Top=142,.Width=207,.Height=13,.Id=1005,.ReadOnly=1,.EditGroup=.editgroup1,.Label$="Wind"},\
         {.editTemp,.kcmldbedit$,.Style=0x50810080,.Left=92,.Top=178,.Width=207,.Height=13,.Id=1004,.ReadOnly=1,.EditGroup=.editgroup1,.Label$="Temperature"},\
         {.ok,.button$,.Style=0x50010001,.Left=331,.Top=6,.Width=50,.Height=14,.Text$="OK",.__Anchor=5,.Id=1},\
         {.cancel,.button$,.Style=0x50010000,.Left=331,.Top=23,.Width=50,.Height=14,.Text$="Cancel",.__Anchor=5,.Id=2},\
         {.editgroup1,.editgroup$,.Left=21,.Top=66,.Width=288,.Height=168,.Id=1001},\
         {.editgroup2,.editgroup$,.Left=21,.Top=12,.Width=286,.Height=33,.Id=1000}
        
        LOCAL DIM loc$100,wind$100,sky$100,temp$100,humidity$100,pressure$100,vis$100
        + DEFEVENT frmWeather.editControl1.Validate()
            s.getSummary(..ValidateText$,REDIM loc$,REDIM wind$,REDIM sky$,REDIM temp$,REDIM humidity$,REDIM pressure$,REDIM vis$)
            ERROR DO
                RETURN FALSE
            END DO
            .editLocation.Text$ = loc$
            .editSky.Text$ = sky$
            .editWind.Text$ = wind$
            .editTemp.Text$ = temp$
        END EVENT
    FORM END frmWeather

Using Document Style

There are two types of SOAP envelope style, RPC and Document. The former is more conventional in that the WSDL defines the arguments passed and returned in the method call whereas the latter passed documents as arguments and leaves the definition of the document to the applications.

KCML SOAP supports the document style by setting a mode for the SOAP object when it is created using the DOC or LIT options to [CREATE](CREATE.htm). The programmer must create and parse the documents/arguments themselves. The code example below calls the same method as before. This time the argument is specified using XML and the result is received as a string. The programmer must know the format of the argument and the argument name. In this situation KCML is acting solely as a transport.

DOC

The user passed data is wrapped in the method name. Then this is sent in the SOAP body.


    s.method1("<arg1>a</arg1><arg2>b</arg2>")


    <body>
    <method1>
            <arg1>a</arg1><arg2>b</arg2>
    </method1>
    </body>

LIT

Everything is directly passed in the SOAP body.


    s.method1("<method1><arg1>a</arg1><arg2>b</arg2></method1>")


    <body>
    <method1><arg1>a</arg1><arg2>b</arg2></method1>
    </body>

\

Here is another way to call the above [example](#weatherexample) in the document style


    DIM opt$="PROXY=proxy:8080, DOC=Y"
    DIM a$400
    OBJECT s = CREATE "SOAP","http://live.capescience.com/wsdl/AirportWeather.wsdl",opt$
    ERROR DO
        END
    END DO
    a$ = s.getSummary$("<arg0>EGLL</arg0>")

    OBJECT s = NULL
    END

The result assigned to a\$ is:


    <location>London / Heathrow Airport, UnitedKingdom</location>
    <wind>from the ESE(110 degrees) at 13 MPH (11 KT) (direction variable)</wind>
    <sky></sky>
    <temp>77 F (25 C)</temp>
    <humidity>44%</humidity>
    <pressure>30.03 in. Hg (1017 hPa)</pressure>
    <visibility>greater than 7 mile(s)</visibility>

This would require parsing from the programmer before it could be used. NOTE: This is not strictly valid XML since there is no root node.
