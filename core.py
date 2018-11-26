import os
import sys

print "> Starting....\n"
print "> PyUp is checking if pip is installed......\n"

# Here the code to do after for cheking if yes or no the pip is installed
try:
    import pip
    print "> Pip is present."
    print "----------------------------------------------------------------------------\n"
    print "> PyUp is installing pip-review .....\n"
    os.system("pip install pip-review")
    os.system("pip-review --auto")
    print "----------------------------------------------------------------------------\n"
    print "> PyUp has updated all your python packages."
except ImportError:
    print "> Pip is not present."
    print "----------------------------------------------------------------------------\n"
    print "> Please use this link to install PIP FIRST: https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation"
    sys.exit()
stop_theclosingcmd = raw_input(".")