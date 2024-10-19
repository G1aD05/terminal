# Simple Terminal

## Commands
**```echo``` -- echo \<text\>\
```mkvar``` -- mkvar \<var name\> \<value\>\
```chvar``` -- chvar \<var name\> \<new value\>\
```delvar``` -- delvar \<var name\>\
```cd``` -- cd \<dir\>\
```ls``` -- ls (current dir)\
```ls -d``` -- ls \<dir>\
```read``` -- read \<file dir>\
```rmv -f``` -- rmv -f \<file dir>\
```rmv -d``` -- rmv -d \<directory dir>\
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
```run``` -- run \<folder name>**

> INFO:\
> Use % on most of the commands to use a variable (ex: echo %variable)\
> Use & as a space in strings (ex: echo Hello,&World)\
> Use \_rand_ to generate a random number (BETA) (ex: echo \_rand_)

## How to use
**1. Download the latest\
2. Open your terminal and type ```python3 /path/to/file/```\
3. You can start using this very basic terminal!**
## Versions
### v1.0.0
**Initial Release.**
### v1.0.3
**Simplified code and made variables acccessible to almost all of the commands.**
### v1.1.0
**Cleaned up code and added new commands.**
### v1.2.1
**Bug fixes, added the new run command, added \_rand_ (generates a random number) and added the & symbol which represents a space.**
### v1.2.3
**Fixed some left over debugging helper things that I accidentally left in**

## Required moduals
### localtz
**Install command: ```pip install localtz```**
### ping3
**Install command: ```pip install ping3```**
### psutil
**Install command: ```pip install psutil```**

## How to Make a Runnable Folder
**Make a folder that looks like this:
\<folder name>\
|-- run.txt\
|-- init.py\
init.py must have a class in it, example:**

```python
class Main:
  def __init__(self, params):
    # Some code
  ```

**run.txt must have the class name and required arguments, example:**

```text
Class Name Here
:ARGS: (Optional if you don't need arguments for your __init__ then don't add this)
requirement
requirement
```
**then you can use this command: ```run <folder name>```**
