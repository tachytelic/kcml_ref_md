<span id="soap"></span>

Converting SOAP services

Previous versions of the Connection Manager only allowed one SOAP service to be defined. The name of the SOAP server program was held in a \<soapstart\> tag. This type of configuration is no longer supported.

To convert to the new specification you need to know the name of the SOAP service. This is the *interface\$* parameter that is passed to ['KCMLObjectExport()](mk:@MSITStore:kcmlrefman.chm::/tmp/kintfld.htm#KCMLObjectExport). The URL used to connect to the SOAP server will be of the form

http://hostname:790/myService/mySoapSrv

where **myService** is the name of the Connection Manager's application [service](systemconf.htm#services), and **mySoapSrv** is the name of the SOAP server's interface.

This would have been defined in *kconf.xml*


    <service>
        <name>myService</name>
        ... ...
        <environment>
            <variable>
                <name>BASE</name>
                <value>/user1/myapp</value>
            </variable>
            <variable>
                <name>START</name>
                <value>$BASE/progs/main.src</value>
            </variable>
            ... ...
        </environment>
        ... ...
        <soapstart>$BASE/progs/soapserver.src</soapstart>
    </service>

The \<soapstart\> tag should be removed and replaced with


        <soap>
            <soapservice>
                <url>mySoapSrv</url>
                <start>$BASE/progs/soapserver.src</start>
                <user>soapuser</user>
            </soapservice>
        </soap>

The \<user\> tag is only relevant on Unix systems, it should contain the name of a valid user account. If there is no value for the \<user\> tag, then the SOAP server will be executed by the **root** super-user.

The URL that is used to connect remains unchanged:

http://hostname:790/myService/mySoapSrv

##### See Also:

[KCML SOAP servers](mk:@MSITStore:kcmlrefman.chm::/soapserver.htm) [Connection Mananger SOAP services](websoap.htm)
