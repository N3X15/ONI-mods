# Nightinggale's ONI Mods
Since Nightinggale [sic] appears to have fallen off the face of the planet, here is my attempt at fixing their mods post LU-372041.

<table>
<tr><th>Tested Against:</th><td>LU-372041</td></tr>
</table>

## Downloading

You'll need:

 * [git](https://git-scm.org)

Do:

1. git clone https://github.com/N3X15/ONI-Mods.git

## Building

### Windows

0. You will need to install Visual Studio 2019.
1. Run `BUILD.exe` to build everything and install it to `$HOME/Documents/Klein/Oxygen Not Included/mods/dev`.

### Linux
You're SOL:  My poor Linux laptop doesn't have the power to run this game, and the buildsystem is dependent on VS2019.  I may change the buildsystem to nant/[whatever the popular CLI build system for C# is] in the future, if there's enough demand.

## BUILD.exe
*AKA: I don't trust this .exe, tell me how to build it!*

BUILD.exe is simply BUILD.py turned into a single-file EXE for Windows users.

To build it, you'll need:

 * &gt;= [Python 3.6 + pip](https://python.org) (`choco install -y python3`)
 * git + [git lfs](https://git-lfs.github.com/)
 * [Visual Studio C++ 14 for Python](https://wiki.python.org/moin/WindowsCompilers#Microsoft_Visual_C.2B-.2B-_14.2_standalone:_Build_Tools_for_Visual_Studio_2019_.28x86.2C_x64.2C_ARM.2C_ARM64.29)
 * N3X15's `buildtools` library (`pip install git+https://gitlab.com/N3X15/python-build-tools.git`)
   * Yes, this library is a mess and pulls in tons of dependencies. I know.
 * pyinstaller (`pip install pyinstaller`)

After all that, just run MKBUILD.bat to invoke pyinstaller. BUILD.exe will be overwritten with the new one.
