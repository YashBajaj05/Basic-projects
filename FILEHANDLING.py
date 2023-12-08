from pathlib import Path
import os

def create_folder():
    name = input("tell your new folder name : ")
    path = Path(name)
    path.mkdir()
    print(f"successfully created a folder named {name}")

def list_files_and_folder():
    path = Path('')
    items = list(path.rglob("*"))
    for i , items in enumerate(items):
        print(f"{i + 1} : {items}")

def update_folder():
    try:
        list_files_and_folder()
        old_name = input("which folder you want to update : ")
        path = Path(old_name)
        if path.exists() and path.is_dir():
            name = input("tell your new name : ")
            new_path = Path(name)
            path.rename(new_path)
            print("name changed successfully")
        else:
            print(f"no folder name {old_name} exists try again")
    except Exception as e:
        print(f"An error occured {e} try again")

def delete_folder():
    try:

        list_files_and_folder()
        name = input("tell what to delete : ")
        path = Path(name)
        if path.exists() and path.is_dir():
            path.rmdir()
        else:
            print(f"name {name} doesn't exist")
    except Exception as e:
        print(f"an error occured {e} please try again")

def createFile():
    list_files_and_folder()
    try:
        name = input("please tell your name of file with extension : ")
        path = Path(name)
        if not path.exists():
            with open(name,"w") as file:
                data = input("write your content : ")
                file.write(data)
            print("succesfully created your file")
        else:
            print("error file name already exist")
    except Exception as e:
        print(f" An error occured {e}")


def updatefile():
    try:
        
        list_files_and_folder()
        name = input("please tell file name that you want to update : ")
        path = Path(name)
        if path.exists() and path.is_file():
            print("operations")
            print("1 . Renaming the file")
            print("2 . Append content")
            print("3 . Overwrite the file")
            choice = input("please tell an option")
            if choice == "1":
                newname = input("Enter the new name with extension : ")
                new_path = Path(newname)        
                if not new_path.exists():
                    path.rename(new_path)
                    print(f"file {name} renamed to {newname}")          
                else:
                    print("file alreday exist")        
            elif choice == "2":
                with open(name,"a") as file:
                    data = input("please tell what you want to append : ")
                    file.write(" " + data)
                print("successfully appended")     
            elif choice == "3":
                with open(name,"w") as file:
                    data = input("please tell what you want in your file : ")
                    file.write(data)
                print("successfully appended")
        else:
            print("file does not exist")

    except Exception as e:
        print(f"an error occured {e}")
        
def deletefile():
    try:
        list_files_and_folder()
        name = input("please enter the name of file you want to delete : ")
        path = Path(name)
        if path.exists() and path.is_file():
            path.unlink()
            print("file deleted successfully")
        else:
            print(f"file {name} does not exist")
    except Exception as e:
        print(f"An error occured {e}")
    
def readfile():
    try:
        list_files_and_folder()
        name = input("please tell your file name : ")
        path = Path(name)
        if path.exists() and path.is_file():
            with open(name,"r") as file:
                content = file.read()
                print(f"content of {name} :\n{content}")

        else:
            print(f"Error file {name} does not exist")
    
    except Exception as e:
        print(f"an error occured as {e}")
    

while True:
    print("press 1 for creating a folder")
    print("press 2 for read a folder")
    print("press 3 for updating a folder")
    print("press 4 for deleting a folder")
    print("press 5 for creating a file")
    print("press 6 for updating a file")
    print("press 7 for deleting a file")
    print("press 8 for reading a file")
    print("press 0 for exiting the application")
    z = input("tell what you want to do : ")

    if z == "1":
        create_folder()
    
    elif z == "2":
        list_files_and_folder()
    
    elif z == "3":
        update_folder()
    
    elif z == "4":
        delete_folder()
    
    elif z == "5":
        createFile()
    
    elif z == "6":
        updatefile()
    
    elif z == "7":
        deletefile()
    
    elif z == "8":
        readfile()
    
    elif z == "0":
        exit(0)
    
    else:
        print("Please provide a number between 0 & 8")




    
