import os
import sys

print "PyUp is checking if pip is installed on this machine......"

# Here the code to do after for cheking if yes or no the pip is installed
try:
    import pip
    print "Pip is present."
    print "-------------------------"
    print "PyUp is installing pip-review ....."
    os.system("pip install pip-review")
    os.system("pip review")
    os.system("pip-review --auto")
except ImportError:
    print "Pip is not present."
    print "-------------------------"
    print "Please use this link to install PIP FIRST: https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation"