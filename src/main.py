import datetime
import os
import shutil
import platform
import ping3 as p3
import tzlocal as tz
import psutil


class Main:
    def __init__(self, args):
        global vars, history
        self.args = args
        self.save = None
        self.prev_dir = os.getcwd()
        self.vars = vars
        self.tz = tz.get_localzone()
        self.history_dat = history
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
            case "ping":
                self.ping()
            case "psd":
                self.psd()
            case "history":
                self.history()
            case "pcp":
                self.pcp()
            case _:
                print("Error: Command not found!")

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
ping -- ping <host name>
history -- (lists command history)
history -a -- history -a <list amount>
pcp -- (prints the current processes)
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
            os.remove(self.parse_variable(self.args[2]))
        elif self.args[1] == '-d':
            os.rmdir(self.parse_variable(self.args[2]))

    def move(self):
        shutil.move(self.parse_variable(self.args[1]), self.parse_variable(self.args[2]))

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def make(self):
        if self.args[1] == '-d':
            os.mkdir(self.parse_variable(self.args[2]))
        if self.args[1] == '-f':
            with open(self.vars.get(self.parse_variable(self.args[2])), 'w') as file:
                file.write('')
                file.close()

    def copy(self):
        shutil.copy(self.parse_variable(self.args[1]), self.parse_variable(self.args[2]))

    def time(self):
        if len(self.args) > 1:
            if self.args[1] == '-format':
                print(datetime.datetime.now(self.tz).strftime(self.parse_variable(self.args[2])))
        else:
            print(datetime.datetime.now(self.tz).strftime('%Y-%m-%d %H:%M:%S'))

    def pwd(self):
        print(os.getcwd())

    def ping(self):
        host = self.parse_variable(self.args[1])
        rtt = p3.ping(host)
        if rtt is not None:
            print(f"Ping to {host} successful. RTT: {rtt} ms")
        else:
            print(f"Failed to ping {host}.")

    def psd(self):
        print("System data:")
        print(platform.system())
        print(platform.release())
        print(platform.version())
        print(platform.machine())
        print(platform.processor())
        print(platform.architecture())

    def history(self):
        if len(self.args) >= 2:
            if self.args[1] == "-a":
                print(self.history_dat[:int(self.parse_variable(self.args[2]))])
        else:
            print(self.history_dat)

    def pcp(self):
        for process in psutil.process_iter(['pid', 'name']):
            print(f"PID: {process.info['pid']}, Name: {process.info['name']}")

    def return_vars(self):
        return self.vars

    def parse_variable(self, _var: str) -> str:
        if _var.startswith("%"):
            return self.vars.get(_var[1:])
        else:
            return _var


if __name__ == '__main__':
    args = []
    vars = {}
    history = []
    while True:
        inp = input(f'{os.getcwd()} % ')
        args.clear()
        for i in inp.split(' '):
            args.append(i)
        try:
            vars.update(Main(args).return_vars())
            history.append(inp)
        except:
            print('Error: Failed to execute command!')
