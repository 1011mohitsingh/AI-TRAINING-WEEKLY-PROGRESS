# Global variable vs  local variable
x = "awesome"
def myfunc(): # global variale
    print("Python is " + x)

myfunc()

def my2func():
    x = "fasntastic"
    print("python is "+ x)

my2func()
print("python is "+x)

