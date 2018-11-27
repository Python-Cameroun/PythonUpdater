import os
import sys

print "> Starting....\n"
print "> PyUp is checking if pip is installed......\n"
separator = "----------------------------------------------------------------------------\n"
# Here the code to do after for cheking if yes or no the pip is installed
try:
    import pip
    print "> PyUp: Pip is present.\n"
    print separator
    print "> PyUp: checking for pip-review .....\n"
    try:
        import pip_review
        print "> PyUp: pip-review is present.\n"
    except:
        print "> PyUp: installing pip-review .....\n"
        os.system("pip install pip-review")
    os.system("pip-review --auto")
    print separator
    print "> PyUp: All your python packages updated successfully.\n"
    print separator
except ImportError:
    print "> Pip is not present."
    print separator
    installPIP = raw_input("> PyUp: Do you want to install it using your browser? (Y/N): ")
    print separator
    if installPIP.lower() == "y":
        print "> PyUp: Opening in the browser....\n"
        try:
            import webbrowser
        except:
            print "> PyUp: You don't have webbrowser installed\n"
            print separator
            os.system("pip install webbrowser")
        webbrowser.open('https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation')
        print separator
    else:
        print "> PyUp: Please use this link to install PIP FIRST, otherwise PyUp is not able to work: https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation"
    sys.exit()
stop_theclosingcmd = raw_input(".")