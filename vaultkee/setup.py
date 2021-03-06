# A simple setup script to create an executable using PyQt4. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# PyQt4app.py is a very simple type of PyQt4 application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

application_title = "VaultKee" #what you want to application to be called
main_python_file = "vaultkee.py" #the name of the python file you use to run the program

import sys
import requests.certs

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = ["atexit","re","core","requests","requests.packages","keyring","keyring.backends.file","keyring.backends.Gnome","keyring.backends.OS_X",
            "keyring.backends.Windows","keyring.backends._win_crypto","keyring.backends.keyczar","keyring.backends.multi",
            "keyring.backends.Google","keyring.backends.SecretService","keyring.backends.pyfs","keyring.backends.kwallet"]
include_files = ['cacert.pem','resources/add.png', 'resources/connect.png', 'resources/delete.png',
                 'resources/icon_128.png', 'resources/images.qrc', 'resources/refresh.png',
                 'resources/visible.png', 'resources/bg.png', 'resources/copy.png',
                 'resources/exit.png', 'resources/icon_48.png', 'resources/key.png', 'resources/lock.png',
                 'resources/save.png', 'ui/main.ui', 'ui/secret.ui', 'ui/login.ui', 'ui/error.ui']

setup(
        name = "VaultKee",
        version = "0.1.2015.06.10",
        description = "Open source graphical frontend to Vault",
        options = {"build_exe" : {"includes" : includes, 'include_files': include_files }},
        executables = [Executable(main_python_file, base = base)])

