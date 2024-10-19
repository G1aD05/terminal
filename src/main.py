import datetime
import os
import shutil
import platform
import ping3 as p3
import tzlocal as tz
import psutil
import random
import importlib.util


class Main:
    def __init__(self, args):
        global vars, history
        self.args = args
        self.save = None
        self.prev_dir = os.getcwd()
        self.vars = vars
        self.tz = tz.get_localzone()
        self.history_dat = history
        self.file_lines = []
        os.chdir(self.prev_dir)
        self.parse_cmd()

    def parse_cmd(self):
        global debug
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
            case "run":
                self.run()
            case "debug":
                if len(self.args) >= 1:
                    if self.args[1] == "off":
                        print("Debug mode off")
                        debug = False
                    elif self.args[1] == "on":
                        print("Debug mode on")
                        debug = True
            case "exit":
                exit()
            case "!":
                self.shell_run()
            case "input":
                self.input()
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
pcp -- (prints the current processes)
run -- run <folder name>
! -- ! <file name> (ex: ! exec.txt)
INFO:
Use % on most of the commands to use a variable (ex: echo %variable)
Use & as a space in strings (ex: echo Hello,&World)
Use _rand_ to generate a random number (BETA) (ex: echo _rand_)
""")

    def echo(self):
        print(self.parse_type(self.args[1]))

    def mkvar(self):
        self.vars.update({self.parse_string(self.args[1]): self.parse_type(self.args[2])})

    def chvar(self):
        self.vars[self.parse_type(self.args[1])] = self.parse_type(self.args[2])

    def delvar(self):
        self.vars.pop(self.parse_type(self.args[1]))

    def cd(self):
        os.chdir(self.parse_type(self.args[1]))

    def ls(self):
        if len(self.args[1:]) > 0:
            if self.args[1] == '-d':
                os.chdir(self.parse_type(self.args[2]))
                for i in os.listdir():
                    print(i)
                os.chdir(self.prev_dir)
        else:
            for i in os.listdir():
                print(i)

    def read(self):
        print(open(self.parse_type(self.args[1]), 'r').read())

    def rmv(self):
        if self.args[1] == '-f':
            os.remove(self.parse_type(self.args[2]))
        elif self.args[1] == '-d':
            os.rmdir(self.parse_type(self.args[2]))

    def move(self):
        shutil.move(self.parse_type(self.args[1]), self.parse_type(self.args[2]))

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def make(self):
        if self.args[1] == '-d':
            os.mkdir(self.parse_type(self.args[2]))
        elif self.args[1] == '-f':
            with open(self.parse_type(self.args[2]), 'w') as file:
                file.write('')
                file.close()

    def copy(self):
        shutil.copy(self.parse_type(self.args[1]), self.parse_type(self.args[2]))

    def time(self):
        if len(self.args) > 1:
            if self.args[1] == '-format':
                print(datetime.datetime.now(self.tz).strftime(self.parse_type(self.args[2])))
        else:
            print(datetime.datetime.now(self.tz).strftime('%Y-%m-%d %H:%M:%S'))

    def pwd(self):
        print(os.getcwd())

    def ping(self):
        host = self.parse_type(self.args[1])
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
        for i in self.history_dat:
            print(i)

    def pcp(self):
        for process in psutil.process_iter(['pid', 'name']):
            print(f"PID: {process.info['pid']}, Name: {process.info['name']}")

    def run(self):
        global params
        self.prev_dir = os.getcwd()
        os.chdir(self.args[1])
        for line in open("run.txt", 'r').read().split('\n'):
            self.file_lines.append(line)
        spec = importlib.util.spec_from_file_location("init", "init.py")
        script = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(script)
        if len(self.file_lines) > 1:
            if self.file_lines[1] == ":ARGS:":
                params = []
                for i in range(len(self.file_lines)):
                    params.append(self.file_lines[i])
                params = params[2:]
        if hasattr(script, self.file_lines[0]):
            klass = getattr(script, self.file_lines[0])
            instance = klass(*params)
            if hasattr(instance, self.file_lines[0]):
                method = getattr(instance, self.file_lines[0])
                method()
        os.chdir(self.prev_dir)

    def shell_run(self):
        lines = []
        parsed_lines = []
        if os.path.isfile(self.args[1]):
            for line in open(self.args[1], 'r').read().split('\n'):
                lines.append(line)
            for i in range(len(lines)):
                parsed_lines.append(lines[i].split(" "))
            for i in range(len(parsed_lines)):
                self.args = parsed_lines[i]
                self.parse_cmd()

    def input(self):
        global out
        out = input(self.parse_type(self.args[1]))

    def return_vars(self) -> dict:
        return self.vars

    def parse_variable(self, _var: str) -> str:
        splits = []
        _str = ""
        if "%" in _var:
            for split in _var.split(" "):
                splits.append(split)
            for i in range(len(splits)):
                if splits[i].startswith("%"):
                    splits[i] = self.vars.get(splits[i][1:])
            for x in range(len(splits)):
                if not x == 0:
                    _str = _str + " " + splits[x]
                else:
                    _str = _str + splits[x]
            return _str
        else:
            return _var

    def parse_type(self, _str):
        _str = self.parse_string(_str)
        _str = self.detect_rand(_str)
        _str = self.det_ats(_str)
        _str = self.parse_variable(_str)
        return _str

    @staticmethod
    def parse_string(_string: str) -> str:
        if "&" in _string:
            _string = _string.replace("&", " ")
            return _string
        else:
            return _string

    @staticmethod
    def detect_rand(_string: str) -> str:
        if "_rand_" in _string:
            return _string.replace("_rand_", str(random.randint(0, 100)))
        else:
            return _string

    @staticmethod
    def det_ats(_str):
        global out
        if "@out" in _str:
            _str = _str.replace("@out", out)
            return _str
        else:
            return _str


if __name__ == '__main__':
    args = []
    vars = {}
    history = []
    debug = False
    params = []
    out = ""
    while True:
        if not debug:
            inp = input(f'{os.getcwd()} % ')
            args.clear()
            for i in inp.split(' '):
                args.append(i)
            try:
                vars.update(Main(args).return_vars())
                history.append(inp)
            except:
                print("Error: Failed to execute command!")

        elif debug:
            inp = input(f'{os.getcwd()} % ')
            args.clear()
            for i in inp.split(' '):
                args.append(i)

            vars.update(Main(args).return_vars())
            history.append(inp)
