 global variables 
# variables which are created outside the function
#they can be used outside the fun.

x= 'john'

def myfunc():
    x = 'peter'
    print("my name is " + x)
    print(x) 

    myfunc() 
    ## we write comments in pythonby using a #