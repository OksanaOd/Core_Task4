#import pathlib
import sys 
from pathlib import Path
#from  colorama import init, Fore, Style
import colorama

def main():
    if len(sys.argv)<2:
        user_input =''
    else:
        user_input=sys.argv[1]
    print(user_input)
    path=Path(user_input)
    if path.exists():
        if path.is_dir():
            items=path.glob('**/*')#glob('*.py')#iterdir()
            for item in items:
                print(item)
        else:
            print(f'{path.absolute} is noe exists')
    #path.absolute(user_input)
    #items=path.glob('**/*')
    #print(items)
    
if __name__ == '__main__':
    main()