import os
import socket

def repl():
    name = os.getenv("USER")
    host_name = socket.gethostname()
    while True:
        try:
            user_input = input(f"{name}@{host_name}:~ $ ").strip()

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
