from os import system as s
from os import chdir as cd
print("SHELL OPENED, use gen.py [github-name] or gen.py to setup MARK.1 env")
class CanProsessDirName(FileNotFoundError): pass
while 1:
    a = input()
    if a == "exit":
        exit()
    elif a[:3] == "cd ":
        try:
            cd(a[3:])
        except:
            raise CanProsessDirName("no file name : {}".format(a[:3]))
    else:
        s(a)