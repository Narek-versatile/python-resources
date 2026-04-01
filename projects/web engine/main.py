import os
import search_engine
import time
import sys

def proc():
    print("Processing", end='')
    sys.stdout.flush()
    time.sleep(0.5)
    
    print(".", end='')
    sys.stdout.flush()
    time.sleep(0.5)

    print(".", end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(".", end = '')
    sys.stdout.flush()
    time.sleep(0.5)
    print("\n\n")
    #flushi patcharov 20 rope gnac...




def print_menu():
    x = """=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
=~=~Basic Google Search Engine=~=~
=~=~=~=Powered By ChatGPT~=~=~=~=~
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~"""
    print(x)

def do_input(inp):
    if inp == 1:
        #index
        proc()
        # print("\n\nhello from debug")

        folder = input("Indexing Folder: ")
        print(google.index_web_pages(folder))
    
    if inp == 2:
        #search
        proc()

    if inp == 3:
        #view file
        proc()
        lst = list(google.web_pages.keys())
        print("_-_-_-_-_-_")
        for nm, pg in enumerate(lst, start=1):
            print(f"{nm}) {pg}")
        print("_-_-_-_-_-_")
        
    
    if inp ==4:
        #exit
        proc()
        print("Danke!\n")
        sys.exit()

def tackle_inp(inp):
    if not inp:
        return
    if not inp[0].isnumeric():
        return
    inp = int(inp[0])
    print(inp)

    if inp<1 or inp>4:
        print("""=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
=~=~=~=~=Invalid input=~=~=~=~=~=~""")
        return
    #function call for identifying and calling the needed service
    do_input(inp)
    input("""
    
    
    
    
Press ENTER to Continue... """)
    os.system('cls')



def mainf():
    os.system('cls')
    while(True):
        
        print_menu()
        inp = input("""-1- Index Web Pages
-2- Search
-3- View File Content
-4- Exit
Choose an option:""")
        os.system('cls')
        tackle_inp(inp)




if __name__ == "__main__":
    google = search_engine.BasicSearchEngine("cache.json")
    mainf()