import sys
import pathlib
from colorama import Fore, Style, init

def show_directory(dir_way, level=0):
    if not dir_way.is_dir():
        print(Fore.RED+ f"{dir_way} is not a directory")
        return
    for item in dir_way.iterdir():
        lev= " " * level
        if item.is_dir():            
            print(Fore.BLUE+f"{lev}{item.name}/")
            show_directory(item, level+1)
        else:
            print(Fore.GREEN+f"{lev}{item.name}")

def main():
    if len(sys.argv) !=2:
        print(Fore.YELLOW+"Input way to directory")
        sys.exit(1)
    dir_way=pathlib.Path(sys.argv[1])
    if not dir_way.exists():
        print(Fore.RED+f"{dir_way} is not exist!")
        sys.exit(1)

    show_directory(dir_way) 

if __name__=="__main__":
    main()

#python "C:\GO IT\python\Core_Task4\Core4_Task_3.py" "C:\GO IT\python\Core_Task4"
#python "C:\GO IT\python\Core_Task4\Core4_Task_3.py" "C:\GO IT\python\Core_Task3"
  
