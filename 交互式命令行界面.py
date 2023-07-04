import cmd
import os
import socket
import shutil

class MySystem(cmd.Cmd):
    print("Hello, 这是基于终端的系统程序，交互式命令行界面！")
    prompt = '输入@$>>> '
    current_directory = ':'

    def do_hello(self, inp):
        print("Hello, 我是李思明!")

    def do_ls(self, inp):
            files = os.listdir('.')
            for file in files:
                print(file)

    def do_cd(self, inp):
        if inp:
            try:
                os.chdir(inp)
                self.current_directory = os.getcwd()
            except FileNotFoundError:
                print("Directory does not exist.")
        else:
            self.current_directory = os.getcwd()

    def do_rm(self, inp):
        if inp:
            try:
                if os.path.isfile(inp):
                    os.remove(inp)
                    print(f"Removed file {inp}")
                elif os.path.isdir(inp):
                    shutil.rmtree(inp)
                    print(f"Removed directory {inp}")
                else:
                    print(f"No such file or directory: {inp}")
            except PermissionError:
                print(f"Permission denied: {inp}")
        else:
            print("Please provide a file or directory name.")

    def do_nano(self, inp):
        os.system(f'nano {inp}')

    def do_cp(self, inp):
        args = inp.split()
        if len(args) >= 2:
            source = args[0]
            destination = args[1]
            try:
                shutil.copy2(source, destination)
                print(f"Copied {source} to {destination}")
            except FileNotFoundError:
                print(f"File not found: {source}")
        else:
            print("Please provide source and destination file names.")

    def do_ip(self, inp):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f"IP Address: {ip_address}")

    def do_mkdir(self, inp):
        if inp:
            try:
                os.mkdir(inp)
                print(f"Created directory {inp}")
            except FileExistsError:
                print(f"Directory {inp} already exists.")
        else:
            print("Please provide a directory name.")

    def do_shell(self, inp):
            output = os.popen(inp).read()
            print(output)

    def do_pwd(self, inp):
            print(os.getcwd())

    def do_touch(self, inp):
            if inp:
                with open(inp, 'a'):
                    os.utime(inp, None)
                    print(f"Created file {inp}")
            else:
                print("Please provide a file name.")

    def do_mv(self, inp):
            args = inp.split()
            if len(args) >= 2:
                source = args[0]
                destination = args[1]
                try:
                    shutil.move(source, destination)
                    print(f"Moved {source} to {destination}")
                except FileNotFoundError:
                    print(f"File not found: {source}")
            else:
                print("Please provide source and destination file names.")

    def do_chmod(self, inp):
            args = inp.split()
            if len(args) == 2:
                mode = int(args[0], 8)
                path = args[1]
                try:
                    os.chmod(path, mode)
                    print(f"Changed permissions of {path} to {args[0]}")
                except FileNotFoundError:
                    print(f"File not found: {path}")
            else:
                print("Usage: chmod <permissions> <file>")

    def do_chown(self, inp):
            args = inp.split()
            if len(args) == 2:
                user = args[0]
                path = args[1]
                try:
                    os.chown(path, user)
                    print(f"Changed owner of {path} to {user}")
                except FileNotFoundError:
                    print(f"File not found: {path}")
            else:
                print("Usage: chown <user> <file>")

    def do_cat(self, inp):
            if inp:
                try:
                    with open(inp, 'r') as f:
                        print(f.read())
                except FileNotFoundError:
                    print(f"File not found: {inp}")
            else:
                print("Please provide a file name.")

    def do_grep(self, inp):
            args = inp.split()
            if len(args) == 2:
                search_text = args[0]
                file_name = args[1]
                try:
                    with open(file_name, 'r') as file:
                        lines = file.readlines()
                        matching_lines = [line for line in lines if search_text in line]
                        for matching_line in matching_lines:
                            print(matching_line.rstrip())
                except FileNotFoundError:
                    print(f"File not found: {file_name}")
            else:
                print("Usage: grep <search_text> <file>")

    def do_head(self, inp):
            args = inp.split()
            if len(args) == 1:
                file_name = args[0]
                try:
                    with open(file_name, 'r') as file:
                        lines = file.readlines()
                        for line in lines[:10]:
                            print(line.rstrip())
                except FileNotFoundError:
                    print(f"File not found: {file_name}")
            else:
                print("Usage: head <file>")

    def do_tail(self, inp):
            args = inp.split()
            if len(args) == 1:
                file_name = args[0]
                try:
                    with open(file_name, 'r') as file:
                        lines = file.readlines()
                        for line in lines[-10:]:
                            print(line.rstrip())
                except FileNotFoundError:
                    print(f"File not found: {file_name}")
            else:
                print("Usage: tail <file>")

    def do_find(self, inp):
            args = inp.split()
            if len(args) == 2:
                directory = args[0]
                file_name = args[1]
                try:
                    for root, dirs, files in os.walk(directory):
                        for file in files:
                            if file_name in file:
                                print(os.path.join(root, file))
                except FileNotFoundError:
                    print(f"Directory not found: {directory}")
            else:
                print("Usage: find <directory> <file_name>")


    def do_quit(self, inp):
        print("终端已经退出！")
        return True

    def do_exit(self, inp):
        print("终端已经退出！")
        return True

    def do_q(self, inp):
        print("终端已经退出！")
        return True

if __name__ == '__main__':
    system = MySystem()
    system.cmdloop()