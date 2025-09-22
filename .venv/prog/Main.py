import os
import socket
import zipfile
from zipfile import *
## VFS name
zipPath = ""
with zipfile.ZipFile(zipPath, "r") as zip_ref:
    fileList = zip_ref.filename

def repl():
    while True:
        try:
            user_input = input(f"{fileList} > ").strip()

            if not user_input:
                continue

            parts = user_input.split()
            cmd, *args = parts

            if cmd == "exit":
                print("bye bye...")
                break
            elif cmd == "ls":
                print(f"cd\nexit\nls\n")
            elif cmd == "cd":
                print(f"still empty comm...")
            else:
                print(f"Error: no such comm '{cmd}'")

        except (EOFError, KeyboardInterrupt):
            print("\n...")
            break


if __name__ == "__main__":
    repl()
