import os
import shutil
import datetime
import tzlocal as tz


class Main:
    def __init__(self, args):
        global vars
        self.args = args
        self.save = None
        self.prev_dir = os.getcwd()
        self.vars = vars
        self._current_dir = None
        self._move_dir = None
        self.tz = tz.get_localzone()
        os.chdir(self.prev_dir)
        self.parse_cmd()

    def parse_cmd(self):
        match self.args[0]:
            case "help":
                self.help()
            case "echo":
                self.echo()
            case "mkvar":
                self.mkvar()
            case "chvar":
                self.chvar()
            case "delvar":
                self.delvar()
            case "cd":
                self.cd()
            case "ls":
                self.ls()
            case "read":
                self.read()
            case "rmv":
                self.rmv()
            case "move":
                self.move()
            case "clear":
                self.clear()
            case "make":
                self.make()
            case "time":
                self.time()
            case "copy":
                self.copy()
            case "pwd":
                self.pwd()
            case _:
                print("Command not found!")

    def help(self):
        print("""
echo -- echo <text>
mkvar -- mkvar <var name> <value>
chvar -- chvar <var name> <new value>
delvar -- delvar <var name>
cd -- cd <dir>
ls -- ls (current dir)
ls -d -- ls <dir>
read -- read <file dir>
rmv -f -- rmv -f <file dir>
rmv -d -- rmv -d <directory dir>
move -- move <dir> <new dir>
clear -- clear (clear terminal)
make -f -- make -f <file name>
make -d -- make -d <directory name>
time -- time
time -format -- time -format <time format>
INFO:
Use % on most of the commands to use a variable (ex: echo %variable)
""")

    def echo(self):
        if self.args[1].startswith("%"):
            print(self.vars.get(self.args[1][1:]))
        elif isinstance(self.args[1], str):
            print(self.args[1])
        else:
            print('Error: Not a string or a variable.')

    def mkvar(self):
        self.vars.update({self.args[1]: self.args[2]})

    def chvar(self):
        self.vars[self.args[1]] = self.args[2]

    def delvar(self):
        self.vars.pop(self.args[1])

    def cd(self):
        if self.args[1].startswith("%"):
            os.chdir(self.vars.get(self.args[1][1:]))
        else:
            os.chdir(self.prev_dir)
            os.chdir(self.args[1])
            self.prev_dir = os.getcwd()

    def ls(self):
        if len(self.args[1:]) > 0:
            if self.args[1] == '-d':
                if self.args[2].startswith("%"):
                    self.prev_dir = os.getcwd()
                    os.chdir(self.vars.get(self.args[2][1:]))
                    for i in os.listdir():
                        print(i)
                    os.chdir(self.prev_dir)
                else:
                    self.prev_dir = os.getcwd()
                    os.chdir(self.args[2])
                    for i in os.listdir():
                        print(i)
                    os.chdir(self.prev_dir)
        else:
            for i in os.listdir():
                print(i)

    def read(self):
        if self.args[1].startswith("%"):
            print(open(self.vars.get(self.args[1][1:]), 'r').read())
        else:
            print(open(self.args[1], 'r').read())

    def rmv(self):
        if self.args[1] == '-f':
            if self.args[2].startswith("%"):
                os.remove(self.vars.get(self.args[2][1:]))
            else:
                os.remove(self.args[2])
        elif self.args[1] == '-d':
            if self.args[2].startswith("%"):
                os.rmdir(self.vars.get(self.args[2][1:]))
            else:
                os.rmdir(self.args[2])

    def move(self):
        if self.startswith(self.args[1], "%"):
            self._current_dir = self.vars.get(self.args[1][1:])
        else:
            self._current_dir = self.args[1]

        if self.startswith(self.args[2], "%"):
            self._move_dir = self.vars.get(self.args[2][1:])
        else:
            self._move_dir = self.args[2]
        shutil.move(self._current_dir, self._move_dir)

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def make(self):
        if self.args[1] == '-d':
            if self.startswith(self.args[2], "%"):
                os.mkdir(self.vars.get(self.args[2][1:]))
            else:
                os.mkdir(self.args[2])
        if self.args[1] == '-f':
            if self.startswith(self.args[2], "%"):
                with open(self.vars.get(self.args[2][1:]), 'w') as file:
                    file.write('')
                    file.close()
            else:
                with open(self.args[2], 'w') as file:
                    file.write('')
                    file.close()

    def copy(self):
        if self.startswith(self.args[1], "%"):
            self._current_dir = self.vars.get(self.args[1][1:])
        else:
            self._current_dir = self.args[1]

        if self.startswith(self.args[2], "%"):
            self._move_dir = self.vars.get(self.args[2][1:])
        else:
            self._move_dir = self.args[2]
        shutil.copy(self._current_dir, self._move_dir)

    def time(self):
        if len(self.args) > 1:
            if self.args[1] == '-format':
                if self.startswith(self.args[2], "%"):
                    print(datetime.datetime.now().strftime(self.vars.get(self.args[2][1:])))
                else:
                    print(datetime.datetime.now(self.tz).strftime(self.args[2]))
        else:
            print(datetime.datetime.now(self.tz).strftime('%Y-%m-%d %H:%M:%S'))

    def pwd(self):
        print(os.getcwd())

    def return_vars(self):
        return self.vars

    def startswith(self, _string: str, _char: str):
        if _string.startswith(_char):
            return True
        else:
            return False


if __name__ == '__main__':
    args = []
    vars = {}
    while True:
        inp = input(f'{os.getcwd()} % ')
        args.clear()
        for i in inp.split(' '):
            args.append(i)
        try:
            vars.update(Main(args).return_vars())
        except:
            print('Error: Failed to execute command!')
