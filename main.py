import os
import time


i=1

def main():
    
    os.system('git init')
    # Get the current working directory
    cwd = os.getcwd()
    os.system('cls')
    print(cwd)
    # Get the list of files and directories in the current working directory
    files = os.listdir(cwd)
    print(files)
    os.system('cls')
    inpu = input("Enter your remote :")
    for file in files:
        command = f"git add {file}"
        os.system(command)
        command2 = f"git commit -m 'Pushed Changes'"
        os.system(command2)
        command3 = f"git push {inpu}"
        os.system(command3)
        i+=1
    time.sleep(0.1)

main()