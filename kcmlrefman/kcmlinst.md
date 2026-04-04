# Installing KCML on Unix

- [Installation system requirements](#prereq)
- [Preparation](#prep)
- [Executing the install script](#exec)
- [Installation](#install)
- [Upgrade](#upgrade)
- [Command line options](#options)
- [Operating system notes](#osnotes)

------------------------------------------------------------------------

### Installation prerequistites

Some combinations of KCML versions and operating systems may require packages installing before installing KCML:

| Operating system | KCML versions | Required packages |
|----|----|----|
| AIX | All | None |
| HP-UX | KCML 6.0 & 6.20 | None |
| Linux | All | ncompress, cpio & xinetd |
| Solaris 8 | KCML 6.0 & 6.20 | None |
| Solaris 10 | KCML 6.20 & 7 | CSWlibgcc-s1 & CSWlibstdc++6, see [Installing KCML for Solaris 10](#solaris10) |
| Unixware | KCML 6.0 & 6.20 | None |

------------------------------------------------------------------------

### Preparation

Select the appropriate version of KCML for your [Unix server](SystemRequirements.htm).

The downloads for Unix servers are in the form of a compressed cpio archive, called an **Image file**. Download this file to a temporary directory, typically */tmp,* on your Unix server. The image file should then be uncompressed using the command


    uncompress IMAGE.Z

Next, you will now need to extract the installation script, *kcmlinst*.\
All versions of KCML on Linux or KCML7


    cpio -iv kcmlinst <IMAGE

KCML 6.00, 6.20 & 6.90 on non-Linux systems:


    cpio -icv kcmlinst <IMAGE

Make sure this script has **execute** permission


    chmod +x kcmlinst

------------------------------------------------------------------------

### Executing the install script

To execute the script, and install KCML, you will need to be the **root** super-user. Execute the install script using


    ./kcmlinst

For Linux systems that do not have a root password, eg Ubuntu, you will need to execute the install script using **sudo**:


    sudo ./kcmlinst

The install script will now display a menu of options


    KCML Administration program Version 2.5
    ================================================================================
    Interrupt key = ^c

                    KCML administration menu
            ========================

            1       INSTALL the KCML Development system
            2       UPGRADE the KCML Development system
            3       REMOVE the KCML Development system
            4       INSTALL/UPGRADE licence file

            9       Exit

            Enter option number (1-9) :

------------------------------------------------------------------------

### Installation

To install KCML take option (1). You will now be prompted for the location of the Image file. Just press \<Return\> for the default of */tmp/IMAGE* or enter the full filename of the image file if it is in a different location. You can choose an **automatic installation** which will choose default settings for the installation. Enter **Y** to run the automatic installation. The install script will now install KCML, after this has completed the script will run the **getid** program to display your server's unique machine ID. Use this number when ordering a KCML licence.

The install script will configure a [network service](mk:@MSITStore:kwebserv.chm::/install.htm) for the [Connection Manager](mk:@MSITStore:kwebserv.chm::/intro.htm). This can be verified by [connecting](mk:@MSITStore:kwebserv.chm::/connserv.htm) a web browser to a URL of the form **http://host:790**

If the script fails with


    Executable files were not compiled for this operating system!

then make sure that the correct version of KCML has been chosen for your system. Also make sure that the operating system is up-to-date, and for 64-bit Linux systems, ensure that 32-bit versions of the C/C++ runtime libraries have been installed.

##### See also:

[Installation prerequistites](#prereq),\
[Operating system requirements](SystemRequirements.htm)

------------------------------------------------------------------------

### Upgrade

The kcmlinst script should also be used to upgrade a KCML installation. Prior to upgrading it is strongly recommended that all KCML users have logged out and that any background KCML processes have been stopped. This can be verified by executing the [bkstat -g](bkstat.htm) command.

After transferring the [appropriate](SystemRequirements.htm) image file to your system, [extract](#prep) and then [execute](#exec) the install script. Take option (2) to upgrade and then enter the location of the IMAGE archive, or just hit \<Return\> to use the default of */tmp/IMAGE*. Then enter the location of the KCML directory you wish to upgrade.

------------------------------------------------------------------------

### Command line options

General form:


    kcmlinst [ -d <dir> -t <tmp_dir> ] [-i] [-u] [-n]

- -d *\<dir\>*: Location of kcml to be installed or upgraded, default */usr/local/kcml*
- -i : Install KCML into */usr/local/kcml* or the directory specified by the -d *dir* option.
- -n : Disable check for running KCMLs when upgrading
- -t *\<tmpdir\>*: Use *tmpdir* for temporary files and the location of the IMAGE cpio archive, default */tmp*
- -u : Upgrade KCML in */usr/local/kcml* or the directory specified by the -d *dir* option.

Normally the kcmlinst script [executes](#exec) interactively. Starting with build 17347 of KCML 6.20, 7.03+, installations and upgrades can be automated using the -d, -t and -u or -i options. For example:


    $ kcmlinst -d /path/to/kcml/directory -t /tmp -i

Would perform an automatic installation of KCML. That installtion could then be later upgraded using


    $ kcmlinst -d /path/to/kcml/directory -t /tmp -u

Both operations require execution as the **root** super-user. The location of the IMAGE cpio archive is in the directory specified by the -t option.

------------------------------------------------------------------------

### Operating system notes

#### Installing KCML for Solaris 10

KCML for Solaris requires the C/C++ runtime libraries from [www.opencsw.org](http://www.opencsw.org) which provides a distribution service of pre-compiled open source software. The packages are installed using OpenCSW's [pkgutil](http://www.opencsw.org/get-it/pkgutil/) package manager which will download and install software from their repository. Package dependencies are automatically resolved:- any extra packages that are required are downloaded and installed. This is very similar to Linux distributions that provide distribution services using package managers like *yum* or *apt-get*. It is recommended that Solaris systems are configured to directly use the distribution service as this provides a very simple mechanism for installing packages that are dependent on other components. The packages are currently available from the default <http://mirror.opencsw.org/opencsw/unstable> repository.

For systems that do not have access to OpenCSW's repository the [CSWlibgcc-s1](http://mirror.opencsw.org/opencsw/unstable/sparc/5.10/libgcc_s1-4.6.2%2cREV%3d2011.12.05-SunOS5.10-sparc-CSW.pkg.gz) & [CSWlibstdc++6](http://mirror.opencsw.org/opencsw/unstable/sparc/5.10/libstdc%2b%2b6-4.6.2%2cREV%3d2011.12.05-SunOS5.10-sparc-CSW.pkg.gz) packages will need to be manually downloaded & transferred onto the system. The package then needs to by uncompressed with *gunzip* before being installed with the Solaris [pkgadd](http://docs.oracle.com/cd/E19963-01/html/821-1462/pkgadd-1m.html) utility.

Installing any OpenCSW package (eg **CSWosslrt** for the OpenSSL 0.9.8 libraries) will most likely depend on the C/C++ libraries thus satisfying the requirements of KCML.
