# KCML: A Brief History

> KCML grew from a Wang 2200 BASIC-2 replacement written in C in 1985 into a cross-platform RAD environment serving over 80,000 end users worldwide.

## Origins: The Wang 2200 Era (1977–1985)

Kerridge Computer Company sold its first system in 1977 — a Wang 2200-based solution for a vehicle dealership in southern England, covering general accounting, inventory control, and vehicle stock management.

The Wang 2200 used an operating system and programming language called **BASIC-2**. BASIC-2 was widely adopted: by the mid-1980s Wang had sold over 20,000 Wang 2200 CPUs. Kerridge grew with it, building several hundred installations in the UK and many more across Europe, Africa, and the Middle East, becoming a dominant force in the motor trade.

Hardware limitations of the Wang 2200 eventually constrained what Kerridge's software could do. In the mid-1980s, Kerridge decided to move to a broader range of platforms.

## First Generation: BASIK (1985–late 1980s)

Development of what would become KCML began at the end of 1985. The goals were to preserve the best parts of the Wang BASIC-2 environment while removing its hardware constraints.

The original implementation was written in C on a Motorola 68000 CPU running an early version of XENIX. Writing in C made porting to other Unix platforms straightforward. The first live production installation ran on an **IBM 6150 RT** under AIX — IBM's Unix. This first version was called **BASIK**.

## Second Generation: KCML (Late 1980s)

As BASIK was adopted by Wang distributors worldwide, the second-generation product was released under the name **KCML**. Key improvements:

- Much improved compatibility with the Wang BASIC-2 language.
- Many new language features.
- Ports to: Motorola 68020/68030, CCI Power 6, IBM RS/6000, Motorola 88000.

## Third Generation (1991–mid-1990s)

Third-generation development began in 1991 and included:

- A **DOS version** of KCML.
- **Novell and NetBIOS LAN versions** (1992).
- A **Windows terminal emulator** (Kerridge Terminal Emulator) supporting both serial and TCP/IP connections to Unix KCML servers — Kerridge's first step toward a true client/server architecture.
- A **native Windows version** of KCML, for the growing DOS KCML user base moving to Windows.
- The ability to call **Windows API routines directly** from KCML programs, available to both Windows and Unix users (the latter via the terminal emulator).

## Today: Fourth Generation

The fourth generation is the current version, aimed at providing a full **Rapid Application Development (RAD)** environment:

- A powerful integrated program editor and debugger.
- A built-in **forms designer** for creating GUI applications.
- A unique client/server architecture designed to work efficiently over wide area networks and the Internet.
- The **KCML Client (Kclient)** — a freely distributable Windows client for displaying KCML forms and text windows.
- Native support for COM and CORBA distributed objects.
- A built-in relational database (KISAM) with both SQL and ISAM access.

## Who Uses KCML?

As of the time of writing, KCML is used by more than **80,000 end users** worldwide. Kerridge's own applications run at 10,000–15,000 sites across Europe, the Middle East, the Far East, and Africa. More than **300 resellers** deploy KCML systems ranging from single-user DOS installations to Unix servers supporting over 2,000 concurrent users.

Application domains include:

- General accounting and inventory management
- Distribution and logistics
- Structural design and stress analysis
- Surveying and cartography
- Hotel management
- Travel booking and reservations
- Electronic auction systems
- Farm management

## Notes

- KCML's Wang BASIC-2 compatibility (through version 3.4) means many legacy Wang programs can be migrated with little or no changes.
- The BASIC-2C / NPL dialect diverged from KCML in the 1990s; compatibility with recent NPL versions is not guaranteed.
- See also: `IntroLangOverview.md` for the technical overview, `IntroProducts.md` for related tools.
