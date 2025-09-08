#!/usr/bin/env python3

def repl():
    vfs_name = "VFS"  # имя виртуальной файловой системы
    while True:
        try:
            # приглашение
            user_input = input(f"[{vfs_name}]$ ").strip()

            if not user_input:  # пустой ввод — пропускаем
                continue

            # разбор ввода на команду и аргументы
            parts = user_input.split()
            cmd, *args = parts

            # обработка команд
            if cmd == "exit":
                print("Выход из эмулятора...")
                break
            elif cmd == "ls":
                print(f"Выполнена команда: {cmd}, аргументы: {args}")
            elif cmd == "cd":
                print(f"Выполнена команда: {cmd}, аргументы: {args}")
            else:
                print(f"Ошибка: неизвестная команда '{cmd}'")

        except (EOFError, KeyboardInterrupt):
            print("\nВыход из эмулятора...")
            break


if __name__ == "__main__":
    repl()
