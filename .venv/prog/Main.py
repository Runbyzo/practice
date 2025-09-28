import os
import socket
import zipfile
import argparse
import subprocess
from zipfile import *

## VFS name
zipPath = "/Users/runbyzo/Documents/VFS.zip"
scriptPath = "/Users/runbyzo/Documents/VFS.zip/ScriptTestFile.txt"

def comEx(cmd):                                                     # cmd command executor
    try:
        if cmd.startswith("echo "):                                 # backs your text f.ex.: >>> echo Hello world! >>> Hello world!
            return cmd[5:]
        elif cmd == "pwd":                                          # shows current directory
            return os.getcwd()
        elif cmd.startswith("cd "):
            path = cmd[3:]                                          #takes path after cmd
            try:
                os.chdir(path)    # changes current directory
                return f"Changed directory to {os.getcwd()}"
            except Exception as e:
                return f"Error: {e}"
        elif cmd == "ls":
            return "cd\nexit\nls\npwd\necho\npwd"                              # show all commas what has CLI
        else:
            return "command failed"                                 # if we dont have such comma
    except Exception as e:                                          # just in case
        return f"Error: {e}"

def scrEx(scriptPath, prompt, showScriptPath = True):               # File executor
    try:
        if showScriptPath:
            scrAbsPath = os.path.abspath(scriptPath)                # found file
            print(f"Start {scrAbsPath}\n\n")

        with open(scriptPath, 'r') as f:                            # open file
            commands = f.readlines()

        for command in commands:                                    # read commas from file
            cmd = command.strip()
            if not cmd or cmd.startswith('#'):
                continue

            print(f"{prompt} {cmd}")                                # print comma
            result = comEx(cmd)
            print(result)

            if result.startswith("Error:"):                         # if in file was smth wrong
                print("Unexpected error")
                return False

        print("Script finished correctly")
        return True

    except FileNotFoundError:                                       # just in case
        print(f"Script wasn't found {scriptPath}")
        return False

    except Exception as e:                                          # just in case
        print(f"Error: {e}")
        return False

def repl(prompt = ">>>"):
    while True:
        try:
            user_input = input(f"{prompt} ").strip()                # takes users input

            if not user_input:
                continue

            parts = user_input.split()                             # makes users input readable for CLI
            cmd, *args = parts

            if cmd == "exit":                                       # if you wanna exit
                print("bye bye...")
                break
            elif cmd == "ls":                                       # commands list
                result = comEx("ls")
                print(result)
            elif cmd == "cd":                                       # directory operations
                if args:
                    result = comEx(f"cd {args[0]}")
                    print(result)
                else:
                    print("Error: cd requires a path argument")
            elif cmd == "pwd":                                      # current directory map
                result = comEx("pwd")
                print(result)
            elif cmd == "echo":                                     # echo user text
                result = comEx(user_input)
                print(result)
            else:                                                   # if user input unexpected command
                result = comEx(user_input)
                print(result)

        except (EOFError, KeyboardInterrupt):                       # just in case...
            print("\n...")
            break

def main():                                                         # main function if what
    parser = argparse.ArgumentParser(description='VFS Emulator')    # make parser object
    parser.add_argument('--vfs-path', type=str, default="/Users/runbyzo/Documents/VFS.zip", # default argues
                        help='Path to VFS zip file')
    parser.add_argument('--prompt', type=str, default=">>>",        # full custom argues
                        help='Prompt for REPL')
    parser.add_argument('--script', type=str,                       # partially custom args
                        help='Path to startup script')

    args = parser.parse_args()

    if os.path.exists(args.vfs_path):                               # checking for existing file
        try:
            with zipfile.ZipFile(args.vfs_path, "r") as zip_ref:
                file_list = zip_ref.namelist()
                print(f"VFS contains {len(file_list)} files")
        except Exception as e:
            print(f"Cannot read VFS file: {e}")
    else:
        print(f"VFS file not found: {args.vfs_path}")

    if args.script:                                                 # executing script file
        print("\nExecuting startup script...")
        success = scrEx(args.script, args.prompt)
        if not success:
            print("Startup script failed, continuing to REPL...")
        print()

    repl(args.prompt)                                               # start repl
if __name__ == "__main__":
    main()
