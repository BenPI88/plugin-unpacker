import os
def clear():
  os.system("clear")
def logo():
  print("d8888b. db      db    db  d888b  d888888b d8b   db      db    db d8b   db d8888b.  .d8b.   .o88b. db   dD d88888b d8888b. \n88  `8D 88      88    88 88' Y8b   `88'   888o  88      88    88 888o  88 88  `8D d8' `8b d8P  Y8 88 ,8P' 88'     88  `8D \n88oodD' 88      88    88 88         88    88V8o 88      88    88 88V8o 88 88oodD' 88ooo88 8P      88,8P   88ooooo 88oobY' \n88~~~   88      88    88 88  ooo    88    88 V8o88      88    88 88 V8o88 88~~~   88~~~88 8b      88`8b   88~~~~~ 88`8b   \n88      88booo. 88b  d88 88. ~8~   .88.   88  V888      88b  d88 88  V888 88      88   88 Y8b  d8 88 `88. 88.     88 `88. \n88      Y88888P ~Y8888P'  Y888P  Y888888P VP   V8P      ~Y8888P' VP   V8P 88      YP   YP  `Y88P' YP   YD Y88888P 88   YD\n\n") 

clear()
logo()

print("Minecraft Directory")
dirto=input("")

def reload():
  clear()
  logo()

reload()

print("Place to unpack from")
dirfrom=input("")

reload()

print("Unzipping .zip files...")
os.system("unzip " + dirfrom + "/*.zip")

reload()

print("Copying files to directory...")
os.system("cp " + dirfrom, "/*.jar " + dirto + "/*")
