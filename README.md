# Nightinggale's ONI Mods
Since Nightinggale [sic] appears to have fallen off the face of the planet, here is my attempt at fixing their mods post LU-372041.

<table>
<tr><th>Tested Against:</th><td>LU-372041</td></tr>
</table>

## Downloading

You'll need:

 * git
 * git LFS (large file support)

Do:

1. git clone https://github.com/N3X15/ONI-Mods.git

If you forget git-lfs, you will get binary files that are actually 3 lines of text, which will not work very well.

## Building

### Windows

0. You will need to install Visual Studio 2019.
1. Run `BUILD.exe` to build everything and install it to `$HOME/Documents/Klein/Oxygen Not Included/mods/dev`.

## BUILD.exe
*AKA: I don't trust this .exe, tell me how to build it!*

BUILD.exe is simply BUILD.py turned into a single-file EXE for Windows users.

To build it, you'll need:

 * >= Python 3.6 + pip (`choco install -y python3`)
 * git + git lfs
 * Visual Studio Tools for Python
 * N3X15's `buildtools` library (`pip install git+https://gitlab.com/N3X15/python-build-tools.git`)
   * Yes, this library is a mess and pulls in tons of dependencies. I know.
 * pyinstaller (`pip install pyinstaller`)

After all that, just run MKBUILD.bat to invoke pyinstaller. BUILD.exe will be overwritten with the new one.
