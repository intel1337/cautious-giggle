
import os
import time

def main():
    
    # Ask user for the number of empty files to create
    num_files = int(input("How many empty files do you want to create? "))
    
    # Create empty files
    for i in range(num_files):
        file_name = f"empty_file_{i + 1}.txt"  # Naming convention for empty files
        with open(file_name, 'w') as f:
            pass  # Create an empty file
    os.system('git init')

    # Get the current working directory
    cwd = os.getcwd()
    print(cwd)
    # Get the list of files and directories in the current working directory
    files = os.listdir(cwd)
    print(files)
    os.system('cls')
    inpu = input("Enter your remote :")
    for file in files:
        command = f"git add {file}"
        os.system(command)
        command2 = f"git commit -am."
        os.system(command2)
        command3 = f"git push --set-upstream {inpu} master"
        os.system(command3)

main()
