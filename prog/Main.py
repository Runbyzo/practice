import os
import socket
import zipfile
import argparse
import subprocess
from zipfile import *

## VFS name
zipPath = "/Users/runbyzo/Documents/VFS.zip"
scriptPath = "/Users/runbyzo/Documents/ScriptTestFile.txt"

# cmd command executor
def comEx(cmd, args):
    try:
        # backs your text f.ex.: >>> echo Hello world! >>> Hello world!
        if cmd.startswith("echo "):
            return cmd[5:]
        # shows current directory
        elif cmd == "pwd":
            return f"{cmd}{args}"
        # takes path after cmd
        elif cmd.startswith("cd "):
            path = cmd[3:]
            try:
                return f"{cmd}{args}"
            except Exception as e:
                return f"Error: {e}"
        # show all commas what has CLI
        elif cmd == "ls":
            return f"{cmd}{args}"
        # if we dont have such comma
        else:
            return "command failed"
    # just in case
    except Exception as e:
        return f"Error: {e}"

# File executor
def scrEx(scriptPath, prompt, showScriptPath = True, args = None):
    try:
        # found file
        if showScriptPath:
            scrAbsPath = os.path.abspath(scriptPath)
            print(f"Start {scrAbsPath}\n\n")

        # open file
        with open(scriptPath, 'r') as f:
            commands = f.readlines()

        # read commas from file
        for command in commands:
            cmd = command.strip()
            cmd, *args = cmd.split(" ")
            if not cmd or cmd.startswith('#'):
                continue

            # print comma
            print(f"{prompt} {cmd}")
            result = comEx(cmd, args)
            print(result)

            # if in file was smth wrong
            if result.startswith("Error:"):
                print("Unexpected error")
                return False

        print("Script finished correctly")
        return True

    # just in case
    except FileNotFoundError:
        print(f"Script wasn't found {scriptPath}")
        return False

    # just in case
    except Exception as e:
        print(f"Error: {e}")
        return False

def repl(prompt = ">>>"):
    while True:
        try:
            # takes users input
            user_input = input(f"{prompt} ").strip()

            if not user_input:
                continue

            # makes users input readable for CLI
            parts = user_input.split()
            cmd, *args = parts

            # if you wanna exit
            if cmd == "exit":
                print("bye bye...")
                break
            # commands list
            elif cmd == "ls":
                result = comEx(cmd, args)
                print(result)
            # directory operations
            elif cmd == "cd":
                if args:
                    result = comEx(cmd, args)
                    print(result)
                else:
                    print("Error: cd requires a path argument")
            # current directory map
            elif cmd == "pwd":
                result = comEx(cmd, args)
                print(result)
            # echo user text
            elif cmd == "echo":
                result = comEx(cmd, args)
                print(result)
            else:
                # if user input unexpected command
                result = comEx(cmd, args)
                print(result)

        # just in case...
        except (EOFError, KeyboardInterrupt):
            print("\n...")
            break
# main function if what
def main():
    # make parser object
    parser = argparse.ArgumentParser(description='VFS Emulator')
    # default argues
    parser.add_argument('--vfs-path', type=str, default="/Users/runbyzo/Documents/VFS.zip",
                        help='Path to VFS zip file')
    # full custom argues
    parser.add_argument('--prompt', type=str, default=">>>",
                        help='Prompt for REPL')
    # partially custom args
    parser.add_argument('--script', type=str,
                        help='Path to startup script')

    args = parser.parse_args()
    # checking for existing file
    if os.path.exists(args.vfs_path):
        try:
            with zipfile.ZipFile(args.vfs_path, "r") as zip_ref:
                file_list = zip_ref.namelist()
                print(f"VFS contains {len(file_list)} files")
        except Exception as e:
            print(f"Cannot read VFS file: {e}")
    else:
        print(f"VFS file not found: {args.vfs_path}")
    # executing script file
    if args.script:
        print("\nExecuting startup script...")
        success = scrEx(args.script, args.prompt)
        if not success:
            print("Startup script failed, continuing to REPL...")
        print()
    # start repl
    repl(args.prompt)
if __name__ == "__main__":
    main()
