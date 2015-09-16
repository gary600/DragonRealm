# Python Program Builder using cxFreeze
# BuildIns.json is the build instruction file, it tells the program how to compile it.
# BuildIns.json may also be used when the program is installed with GitBuild.py.



import sys
import os
import json
BlankBuildIns = {"doExecute":False,"buildData":{"name":None,"version":None,"description":None,"buildFile":None,"base":None,"options":{}}}
if os.path.exists("buildins.json") == False:
    print("Creating BuildIns.json file... ")
    f = open("buildins.json", "w")
    json.dump(BlankBuildIns, f, indent=4)
    f.close()
    f = None
    raise SystemExit
f = open("buildins.json","r")
BuildIns = json.load(f)
if BuildIns["doExecute"] == False:
    print("doExecute is false!!!")
    raise SystemExit
try:
	start = input("Compile recipe "+sys.argv[1]+"?[Y/n]: ")
except IndexError:
	print("No recipe!")
	raise SystemExit
if start.lower() == "y":
    print("Compiling recipe: "+sys.argv[1])
else:
	print("Abort!")
	raise SystemExit
from cx_Freeze import setup, Executable
try:
    setup(  name = BuildIns["buildData"]["name"],
            version = BuildIns["buildData"]["version"],
            description = BuildIns["buildData"]["description"],
            options = BuildIns["buildData"]["options"],
            executables = [Executable(BuildIns["buildData"]["buildFile"], base=BuildIns["buildData"]["base"],shortcutName=BuildIns["buildData"]["name"])])
except IndexError:
    print("BuildIns.json is invalid!")
    raise SystemExit