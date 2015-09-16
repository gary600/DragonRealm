# DragonRealm
A little ASCII adventure game in Python<br />
This is a little experiment to try to make a cool adventure game in Python.
Currently, branch 1.1.0 is under development. Branches 1.0.* are fully functional (but identical)
## Installation
You can either run it from the source or compile and install it.
* On Windows:
    1. Make sure that [cx_Freeze](http://cx-freeze.sourceforge.net/) is installed
    2. In cmd, cd to the folder with the source code and type:
        * If you want to get a raw EXE file: "python build.py build_exe"
        * If you want an MSI windows installer: "python build.py bdist_msi"
        * If you want to directly install DragonRealm: "python build.py install"
* On Mac:
    1. Make sure that [cx_Freeze](http://cx-freeze.sourceforge.net/) is installed
    2. In terminal, cd to the folder with the source code and type:
        * If you want to get an executable .app package: "python3 build.py bdist_mac"
        * If you want a DMG image containing the .app package: "python3 build.py bdist_dmg"
* On Linux:
    If you are running linux, I think that you probably already know how to do this.