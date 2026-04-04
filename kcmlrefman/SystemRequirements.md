KCML/KClient Operating System Requirements

KCML provides a highly portable application environment. However developments that make use of new Operating System functionality may not be available on older systems. The following tables illustrate the availability, and requirements, of recent developments of the KCML application environment.

### KCML 6.20

| Product | Compatible Systems | [Xerces](xerces.htm) <sup>[(3)](#3)</sup> | [SSL sockets](SSL.htm) | [SOAP WSS](ObjSoap.htm#WSS) | [PAM authentication](mk:@MSITStore:kwebserv.chm::/pam.htm) <sup>[(14)](#14)</sup> | [Secure Connection Manager & KClient-\>KCML Connections](mk:@MSITStore:kwebserv.chm::/secureconn.htm) |
|----|----|----|----|----|----|----|
| KCML AIX43_4.3 | AIX4.3 with PowerPC CPU | No | Yes <sup>[(11)](#11), [(12)](#12)</sup> | Yes <sup>[(11)](#11), [(12)](#12)</sup> | No | Yes <sup>[(11)](#11), [(12)](#12)</sup> |
| KCML AIX52_5.2 | AIX 5.1 & 5.2 with PowerPC CPU | Yes | Yes - requires OpenSSL 0.9.7 <sup>[(10)](#10)</sup> | Yes - requires OpenSSL 0.9.7 <sup>[(10)](#10)</sup> | Yes, AIX5.3 ML11 or higher <sup>[(9)](#9), [(21)](#21)</sup> | Yes - OpenSSL 0.9.7 <sup>[(10)](#10)</sup> |
| KCML AIX53_5.3 | AIX 5.3 ML11 (or later) & AIX 6.1 with Power4 (or higher) CPU <sup>[(23)](#23)</sup> | Yes | Yes - requires OpenSSL 0.9.8 <sup>[(13)](#13)</sup> | Yes - requires OpenSSL 0.9.8 <sup>[(13)](#13)</sup> | Yes <sup>[(21)](#21)</sup> | Yes - requires OpenSSL 0.9.8 <sup>[(13)](#13)</sup> |
| KCML HP9000_B.11.00 | HP-UX 11.00, 11.11 & 11.i with PA-RISC or Itanium CPU | Yes | Yes <sup>[(11)](#11), [(12)](#12), [(15)](#15), [(18)](#18)</sup> | Yes <sup>[(11)](#11), [(12)](#12), [(15)](#15), [(18)](#18)</sup> | Yes | Yes <sup>[(11)](#11), [(12)](#12), [(15)](#15), [(18)](#18)</sup> |
| KCML LINUX_2.4-x86 | Any of the [supported Linux distribtions](#Linux) for x86/x64 CPUs <sup>[(1)](#1)</sup> | Yes | Yes - requires OpenSSL 0.9.7 | Yes - requires OpenSSL 0.9.7 | Yes <sup>[(1)](#1)</sup> | Yes - requires OpenSSL 0.9.7 |
| KCML LINUX_2.6-x86 | Any of the [supported Linux 2.6 distributions](#Linux) for x86/x64 CPUs <sup>[(1)](#1), [(4)](#4)</sup> | Yes | Yes - requires OpenSSL 0.9.8 <sup>[(1)](#1), [(4)](#4)</sup> | Yes - requires OpenSSL 0.9.8 <sup>[(1)](#1), [(4)](#4)</sup> | Yes <sup>[(1)](#1)</sup> | Yes - requires OpenSSL 0.9.8 <sup>[(1)](#1), [(4)](#4)</sup> |
| KCML SUN_5.8 | Solaris 8 or later with Sparc CPU | Yes | Yes <sup>[(12)](#12), [(25)](#25)</sup> | Yes <sup>[(12)](#12), [(25)](#25)</sup> | Yes | Yes <sup>[(12)](#12), [(25)](#25)</sup> |
| KCML SUN_5.10 | Solaris 10 or later with Sparc CPU <sup>[(22)](#22)</sup> | Yes | Yes <sup>[(24)](#24)</sup> | Yes <sup>[(24)](#24)</sup> | Yes | Yes <sup>[(24)](#24)</sup> |
| KCML UNIXWARE_7.0.1 | Unixware 7.0.1 with x86 CPU | No | Yes <sup>[(11)](#11), [(12)](#12), [(15)](#15), [(16)](#16)</sup> | Yes <sup>[(11)](#11), [(12)](#12), [(15)](#15), [(16)](#16)</sup> | No | Yes <sup>[(11)](#11), [(12)](#12), [(15)](#15), [(16)](#16)</sup> |
| KCML UNIXWARE_7.1.1 | Unixware 7.1.1.5 (or later <sup>[19](#19)</sup>) with x86 CPU | Yes <sup>[(16)](#16)</sup> | Yes <sup>[(11)](#11), [(12)](#12), [(15)](#15), [(16)](#16)</sup> | Yes <sup>[(11)](#11), [(12)](#12), [(15)](#15), [(16)](#16)</sup> | No | Yes <sup>[(11)](#11), [(12)](#12), [(15)](#15), [(16)](#16)</sup> |
| KCML Windows | Windows XP SP2 or later incl 32- & 64-bit kernels <sup>[(2)](#2)</sup> | Yes | Yes | Yes - requires OpenSSL 0.9.7 | No | No |

### KCML 6.00

| Operating System             | Large files \> 2Gb <sup>[(5)](#5)</sup> |
|------------------------------|-----------------------------------------|
| AIX4.3                       | Yes                                     |
| AIX5.1+                      | Yes                                     |
| HP-UX 10.20                  | Yes                                     |
| HP-UX 11                     | Yes                                     |
| Linux 2.4+ x86               | Yes                                     |
| Sco OpenServer 5             | No                                      |
| Solaris 8 Sparc              | Yes                                     |
| Unixware 2                   | No                                      |
| Unixware 7                   | Yes                                     |
| Windows <sup>[(2)](#2)</sup> | Yes                                     |

------------------------------------------------------------------------

### KClient

| Operating System | 5.02 | 5.50 | 6.00 | 6.20 | 6.90 |
|----|----|----|----|----|----|
| Windows XP <sup>[(6)](#6)</sup> | Yes | Yes | Yes | Yes | Yes |
| Windows Vista 32 bit<sup>[(6)](#6)</sup> | No | Yes | Yes | Yes | Yes |
| Windows Vista 64 bit<sup>[(6)](#6)</sup> | No | Yes<sup>[(7)](#7)</sup> | Yes<sup>[(7)](#7)</sup> | Yes<sup>[(7)](#7)</sup> | Yes |
| Windows 7 32 bit<sup>[(6)](#6)</sup> | No | Yes | Yes | Yes | Yes |
| Windows 7 64 bit<sup>[(6)](#6)</sup> | No | Yes<sup>[(7)](#7)</sup> | Yes<sup>[(7)](#7)</sup> | Yes<sup>[(7)](#7)</sup> | Yes |
| Windows Server 2003 32 bit | No | Yes | Yes | Yes | Yes |
| Windows Server 2003 64 bit | No | Yes<sup>[(7)](#7)</sup> | Yes<sup>[(7)](#7)</sup> | Yes<sup>[(7)](#7)</sup> | Yes |
| Windows Server 2008 32 bit | No | Yes | Yes | Yes | Yes |
| Windows Server 2008 64 bit | No | Yes<sup>[(7)](#7)</sup> | Yes<sup>[(7)](#7)</sup> | Yes<sup>[(7)](#7)</sup> | Yes |
| Windows Server 2008 R2 | No | Yes<sup>[(7)](#7)</sup> | Yes<sup>[(7)](#7)</sup> | Yes<sup>[(7)](#7)</sup> | Yes |
| Windows Fundamentals | No | No | No | No | No |

KClient supports running in a Terminal Services client such as Citrix or RDP, in which case compatibility is dependent on the server's operating system regardless of the operating system running on the terminal itself

------------------------------------------------------------------------

## Supported Linux Operating Systems

KCML 6 & 7 will run on most Linux distributions. It will require the following packages prior to [installation](kcmlinst.htm):

- **ncompress** & **cpio** - to uncompress and extract files from IMAGE.Z
- **xinetd** - network super-server for the [Connection Manager](mk:@MSITStore:kwebserv.chm::/intro.htm).

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Linux version</th>
<th>Compatible KCML versions</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>CentOS 4 <sup><a href="#7">(7)</a></sup></td>
<td>All</td>
<td>Only provides OpenSSL 0.9.7. You will need to copy the OpenSSL 0.9.8 compatibility libraries for Red Hat 4 from <a href="http://www.kcml.com/download/download.html">KCML Download Area -&gt; Resources for Developers</a> into the KCML directory.<br />
Only supports Apache 2.0 which is <strong>not compatible</strong> with <a href="mod_wcm.htm">mod_wcm.so</a></td>
</tr>
<tr>
<td>CentOS 5</td>
<td>All</td>
<td></td>
</tr>
<tr>
<td>CentOS 6 <sup><a href="#1">(1)</a>, <a href="#20">(20)</a></sup></td>
<td>All</td>
<td><a href="SSL.htm">SSL support</a> requires <strong>openssl098e</strong> package to be installed.</td>
</tr>
<tr>
<td>Debian 5 &amp; 6</td>
<td>All</td>
<td>KCML is only compatible with the 32-bit kernel as 64-bit versions of Debian do not provide a complete runtime environment for 32-bit applications.</td>
</tr>
<tr>
<td>Fedora Core 10 &amp; 11</td>
<td>All</td>
<td></td>
</tr>
<tr>
<td>Fedora Core 12, 13 &amp; 14 <sup><a href="#7">(7)</a></sup></td>
<td>All</td>
<td>Only provides OpenSSL 1.0. You will need to copy the OpenSSL 0.9.8 compatibility libraries for Fedora Core 12 from <a href="http://www.kcml.com/download/download.html">KCML Download Area -&gt; Resources for Developers</a> into the KCML directory.</td>
</tr>
<tr>
<td>Fedora Core 15 or later<sup><a href="#7">(7)</a></sup></td>
<td>7.04.00.17314 or later</td>
<td>Only provides OpenSSL 1.0. You will need to copy the OpenSSL 0.9.8 compatibility libraries for Fedora Core 12 from <a href="http://www.kcml.com/download/download.html">KCML Download Area -&gt; Resources for Developers</a> into the KCML directory.</td>
</tr>
<tr>
<td>Mandriva 2010</td>
<td>All</td>
<td></td>
</tr>
<tr>
<td>Open SuSE 11.1 &amp; 11.2 <sup><a href="#1">(1)</a></sup></td>
<td>All</td>
<td>Use <em>YaST-&gt;System-&gt;System Services (Runlevel)</em> to permanently enable <strong>xinetd</strong></td>
</tr>
<tr>
<td>Open SuSE 11.3 or later <sup><a href="#1">(1)</a>, <a href="#20">(20)</a></sup></td>
<td>All</td>
<td><a href="SSL.htm">SSL support</a> requires <strong>libopenssl0_9_8</strong> package to be installed.<br />
Use <em>YaST-&gt;System-&gt;System Services (Runlevel)</em> to permanently enable <strong>xinetd</strong></td>
</tr>
<tr>
<td>Oracle Enterprise Linux 5</td>
<td>All</td>
<td>Based on RedHat ES 5</td>
</tr>
<tr>
<td>Red Hat ES 3</td>
<td>6.00 &amp; 6.20 only</td>
<td></td>
</tr>
<tr>
<td>Red Hat ES 4 <sup><a href="#7">(7)</a></sup></td>
<td>All</td>
<td>Only provides OpenSSL 0.9.7. You will need to copy the OpenSSL 0.9.8 compatibility libraries for Red Hat 4 from <a href="http://www.kcml.com/download/download.html">KCML Download Area -&gt; Resources for Developers</a> into the KCML directory.<br />
Only supports Apache 2.0 which is <strong>not compatible</strong> with <a href="mod_wcm.htm">mod_wcm.so</a></td>
</tr>
<tr>
<td>Red Hat ES 5</td>
<td>All</td>
<td></td>
</tr>
<tr>
<td>Red Hat ES 6 <sup><a href="#1">(1)</a>, <a href="#20">(20)</a></sup></td>
<td>All</td>
<td><a href="SSL.htm">SSL support</a> requires <strong>openssl098e</strong> package to be installed.</td>
</tr>
<tr>
<td>Ubuntu 8, 9 &amp; 10</td>
<td>All</td>
<td></td>
</tr>
<tr>
<td>Ubuntu 11</td>
<td>All versions of build 17132 or later</td>
<td></td>
</tr>
</tbody>
</table>

- <span id="1"><sup>(1)</sup></span> Linux versions of KCML are compatible with 32- & 64-bit kernels. When running under a 64-bit kernel, KCML will require 32-bit components, eg OpenSSL & PAM
- <span id="2"><sup>(2)</sup></span> Supported versions of Windows are XP Service Pack2, Vista, Windows 7, 2003 Server, 2008 Server
- <span id="3"><sup>(3)</sup></span> The Xerces 2.7 shared library is installed as part of KCML, except for Unixware 7.1.1.5 where Xerces 2.6 is directly built into dyndom.so
- <span id="4"><sup>(4)</sup></span>If SSL or SOAP WSS is required on Linux 2.6 systems that only provide OpenSSL 0.9.7 or 1.0 then install the OpenSSL 0.9.8 compatibility libraries from the [KCML download area -\> Resources for Developers](http://www.kcml.com/download/download.html) into the KCML directory.
- <span id="5"><sup>(5)</sup></span> Requires a filesystem capable of supporting large files \> 2Gb.
- <span id="6"><sup>(6)</sup></span> Home, Professional, Ultimate etc versions do not affect KClient.
- <span id="7"><sup>(7)</sup></span> Requires 64 bit KClient shell extensions available as a separate install.
- <span id="8"><sup>(8)</sup></span> PAM configuration is dependent on the Operating System, see [Connection Manager](mk:@MSITStore:kwebserv.chm::/pam.htm).
- <span id="9"><sup>(9)</sup></span> KCML compiled for AIX5 will authenticate against the local password database (*/etc/passwd*, */etc/security/user*, */etc/security/passwd* ...) when running on AIX5.1 & 5.2. When running under AIX5.3, or later, KCML will authenticate using AIX PAM.
- <span id="10"><sup>(10)</sup></span> OpenSSL 0.9.7 may be an optional package on AIX 5.1 & 5.2 systems. It can be installed from an *openssl-0.9.7...* RPM package on the **Linux Tools for PowerPC** disk.
- <span id="11"><sup>(11)</sup></span> The libcrypto.so & libssl.so libraries are shipped with KCML for older systems that have no native OpenSSL support. A [Secure Connection Manager](mk:@MSITStore:kwebserv.chm::/secureconn.htm) will require these libraries to be copied, or symbolically linked, into */usr/lib*.
- <span id="12"><sup>(12)</sup></span> These operating systems will require KCML 06.20.51.15357 or later.
- <span id="13"><sup>(13)</sup></span> OpenSSL 0.9.8 is an optional package on AIX 5.3 & AIX 6 systems. Install the **openssl.base** & **openssl.license** filesets.
- <span id="14"><sup>(14)</sup></span> PAM configuration is dependent on the Operating System, see [PAM authentication](mk:@MSITStore:kwebserv.chm::/pam.htm).
- <span id="15"><sup>(15)</sup></span> Unixware 7.1 & HP-UX11.11/11i systems can be configured to provide the */dev/urandom* random number source. Contact ADP for futher information.
- <span id="16"><sup>(16)</sup></span> Use of 3rd-party shared libraries will require [\$USEMALLOC](EnvVars.htm#USEMALLOC) to be set on Unixware systems.
- <span id="18"><sup>(18)</sup></span> HP-UX 11.11 requires operating system patch PHSS_26560 : *s700_800 11.11 ld(1) and linker tools cumulative patch*
- <span id="19"><sup>(19)</sup></span> Unixware 7.1.3 requires maintainence pack MP4 (uw713mp4) for bug fix erg712282/fz526486.
- <span id="20"><sup>(20)</sup></span> Operating system uses OpenSSL 1.0.0 as standard, however an OpenSSL 0.9.8 library package can be installed.
- <span id="21"><sup>(21)</sup></span> AIX6.1 ML6 will require the [IZ97416s04.110329.epkg.Z](http://www14.software.ibm.com/webapp/set2/subscriptions/pqvcmjd?mode=18&ID=5412) fix when PAM is configured to authenticate against an LDAP password database.
- <span id="22"><sup>(22)</sup></span> KCML for Solaris 10 requires the CSWlibgcc-s1 & CSWlibstdc++6 packages to be installed **prior** to installing KCML, these are available from [www.opencsw.org](http://www.opencsw.org). For more information see [Installing KCML for Solaris 10](kcmlinst.htm#solaris10)
- <span id="23"><sup>(23)</sup></span> Use the ***prtconf*** or ***lsattr -l proc0 -E*** commands to ascertain the processor type for AIX5.3 or later.\
  Maintenance Level (ML) can be found using the ***oslevel -g*** command or by inspecting */usr/lpp/bos/aix_release.level*
- <span id="24"><sup>(24)</sup></span> KCML SSL support for Solaris 10 requires OpenSSL 0.9.8 which is provided by the CSWosslrt package from [www.opencsw.org](http://www.opencsw.org)
- <span id="25"><sup>(25)</sup></span> Pre-compiled versions of OpenSSL 0.9.7 for Sun Solaris 8 are available from [SunFreeware.com](http://www.sunfreeware.com/)\
