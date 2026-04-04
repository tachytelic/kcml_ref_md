Setting Up The Connection Broker

Installing the connection broker

The broker is installed as part of KCML and added in the startup script alongside [kplicserver](kplicserver.htm#exec). The connection broker is not enabled by default. To do this the appropriate lines in the startup script must be uncommented.


    # Uncomment the following lines if you want the broker to be started automatically

    #if [ /usr/local/kcml/broker ]
    #then
    #        /usr/local/kcml/broker &
    #fi

Configuring the connection broker

There is only one command line option '-v' which will indicate the version number.

The broker reads its configuration from kconf.xml. The settings are stored inside a \<broker\> tag e.g.


    <broker>
            <logfile>broker.log</logfile>
            <loglevel>0</loglevel>
    </broker>

The broker will re-read its configuration if signaled with SIGHUP.

The full list of possible options is:

| Tag | Setting | Unit | Purpose | Default |
|----|----|----|----|----|
| listenport | Listen Port | integer | The port which the broker will listen on for connections | 14600 |
| logfile | Log File | string | Path to the log file | broker.txt |
| loglevel | Log Level | integer | Controls the amount of information written to the log file. A level of 0 will log only critical events whilst the maximum level 9 will log every connecion event. | 1 |
| idletimeout | Idle Timeout | hours | The broker can only support a finite number of sessions. If all available session slots are in use and a new sessions is requested, either the request must be refused or one of the existing sessions will be disconnected. This setting controls how long a session must be idle to become a candidate for disconnection. | 48 |
| conntimeout | Connect Timeout | seconds | When a client connects to the broker it will immediately take up a session slot while the session is being established. To prevent broken/malicious clients using all available slots any new connection must establish a session within this timeout. Any that fail to do this will be disconnected. | 60 |
| nagle | Nagle Algorithm | boolean | The Nagle algorithm is used by network applications to combine multiple small data writes into larger ones in order to make more efficient use of the network by reducing packet overhead. This can cause a lack of responsiveness in interactive applications such as KClient and is disabled by default. | no |

Usually the path to the log file is all that needs to be set.
