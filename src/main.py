import json
import os
import shutil
import datetime


class Main:
    def __init__(self, args):
        self.args = args
        self.save = None
        self.prev_dir = os.getcwd()
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        if not os.path.isfile('vars.json'):
            with open('vars.json', 'w') as f:
                f.write('{}')
        self.vars = json.loads(open('vars.json', 'r').read())
        os.chdir(self.prev_dir)
        self.parse_cmd()

    def parse_cmd(self):
        if self.args[0] == 'help':
            self.help()
        elif self.args[0] == 'echo':
            self.echo()
        elif self.args[0] == 'mkvar':
            self.mkvar()
        elif self.args[0] == 'chvar':
            self.chvar()
        elif self.args[0] == 'delvar':
            self.delvar()
        elif self.args[0] == 'cd':
            self.cd()
        elif self.args[0] == 'ls':
            self.ls()
        elif self.args[0] == 'read':
            self.read()
        elif self.args[0] == 'rmv':
            self.rmv()
        elif self.args[0] == 'move':
            self.move()
        elif self.args[0] == 'clear':
            self.clear()
        elif self.args[0] == 'make':
            self.make()
        elif self.args[0] == 'time':
            self.time()
        elif self.args[0] == 'copy':
            self.copy()
        elif self.args[0] == 'pwd':
            self.pwd()
        else:
            print('Error: Command not found!')

    def help(self):
        print("""
echo -- echo <text>
echo -var -- echo -var <var name>
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
""")

    def echo(self):
        if self.args[1] == '-var':
            print(self.vars.get(self.args[2]))
        elif isinstance(self.args[1], str):
            print(self.args[1])
        else:
            print('Error: Not a string or a variable.')

    def mkvar(self):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.vars.update({self.args[1]: self.args[2]})
        open('vars.json', 'w').write(json.dumps(self.vars))

    def chvar(self):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.vars[self.args[1]] = self.args[2]
        open('vars.json', 'w').write(json.dumps(self.vars))

    def delvar(self):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.vars.pop(self.args[1])
        open('vars.json', 'w').write(json.dumps(self.vars))

    def cd(self):
        os.chdir(self.prev_dir)
        os.chdir(self.args[1])
        self.prev_dir = os.getcwd()

    def ls(self):
        if len(self.args[1:]) > 0:
            if self.args[1] == '-d':
                self.prev_dir = os.getcwd()
                os.chdir(self.args[2])
                for i in os.listdir():
                    print(i)
                os.chdir(self.prev_dir)
        else:
            for i in os.listdir():
                print(i)

    def read(self):
        print(open(self.args[1], 'r').read())

    def rmv(self):
        if self.args[1] == '-f':
            os.remove(self.args[2])
        elif self.args[1] == '-d':
            os.rmdir(self.args[2])

    def move(self):
        shutil.move(self.args[1], self.args[2])

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def make(self):
        if self.args[1] == '-d':
            os.mkdir(self.args[2])
        if self.args[1] == '-f':
            with open(self.args[2], 'w') as file:
                file.write('')
                file.close()

    def copy(self):
        shutil.copy(self.args[1], self.args[2])

    def time(self):
        if len(self.args) > 1:
            if self.args[1] == '-format':
                print(datetime.datetime.now().strftime(self.args[2]))
        else:
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def pwd(self):
        print(os.getcwd())


if __name__ == '__main__':
    args = []
    while True:
        inp = input(f'{os.getcwd()} % ')
        args.clear()
        for i in inp.split(' '):
            args.append(i)
        try:
            Main(args)
        except:
            print('Error: Failed to execute command!')

