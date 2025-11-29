# Terminal

> [!Note]\
> Requires Python 3.x

## Commands
**```echo``` -- echo \<text\>\
```mkvar``` -- mkvar \<var name\> \<value\>\
```chvar``` -- chvar \<var name\> \<new value\>\
```delvar``` -- delvar \<var name\>\
```cd``` -- cd \<dir\>\
```ls``` -- ls (current dir)\
```ls -d``` -- ls \<dir>\
```read``` -- read \<file dir>\
```rmv``` -- rmv \<file/directory>\
```move``` -- move \<dir\> \<new dir\>\
```clear``` -- clear (clear terminal)\
```make``` -f -- make -f \<file name\>\
```make``` -d -- make -d \<directory name\>\
```time``` -- time\
```time -format``` -- time -format \<time format\>\
```ping``` -- ping \<host name\>\
```history``` -- (lists command history)\
```history -a``` -- history -a \<list amount\>\
```pcp``` -- (prints the current processes)\
```input``` -- input <text>\
```!``` -- ! \<file name>\
```zip -u``` -- zip -u \<zip file name> \<directory name>\
```zip -z``` -- zip -z \<zip file name> <directory/file name>\
```kill``` -- kill \<process id>\
```banner``` -- banner \<text>\
```banner -f``` -- banner -f \<text> \<font>\
```dld``` -- dld \<url> \<output name>\
```find``` -- find \<file name> \<search term>\
```timeit``` -- timeit \<command name\> \<args\>**

> [!NOTE]
> Use % on most of the commands to use a variable (ex: echo %variable)\
> Use & as a space in strings (ex: echo Hello,&World)\
> Use \_rand_ to generate a random number (BETA) (ex: echo \_rand_)\
> Use // as a seperator in commands (ex: echo Hello//echo World)\
> Use ; in some of the commands to seperate an arg

## How to use
**1. Download the latest\
2. Open your terminal and type ```python3 /path/to/file/```\
3. You can start using this very basic terminal!**
## Versions
### v1.0.0-beta
**Initial Release.**
### v1.0.3-beta
**Simplified code and made variables acccessible to almost all of the commands.**
### v1.1.0-beta
**Cleaned up code and added new commands.**
### v1.2.1-beta
**Bug fixes, added the new run command, added ```_rand_``` (generates a random number) and added the ```&``` symbol which represents a space.**
### v1.2.3-beta
**Fixed some left over debugging helper things that I accidentally left in**
### v1.3.0-beta
**Improved variable detection system, added the ```input``` (Gets an input from the user access with @out) and ```!``` (Run shell files) commands, and bug fixes**
### v1.3.5-beta
**Added the new ```zip```, ```kill``` and ```banner``` commands, added support for manual arguments for the run command**
### v1.3.7-beta
**Added the new ```dld``` and ```find``` commands, added line coloring**
### v1.4.0
**Added more color coding, enhanced the ```rmv``` command, added command batching by using // and minor bug fixes, also it's out of beta.**
### v1.4.1
**Removed the ```run``` command and replaced it with files matching stuff and added the ```open``` command which opens images**

## Required modules
### tzlocal
**Install command: ```pip install tzlocal```**
### ping3
**Install command: ```pip install ping3```**
### psutil
**Install command: ```pip install psutil```**
### pyfiglet
**Install command: ```pip install pyfiglet```**
### colorama
**Install command: ```pip install colorama```**
### pillow
**Install command: ```pip install pillow```**

### Install all the modules: ```pip install -r requirements.txt```

