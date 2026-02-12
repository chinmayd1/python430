# reduce 
from functools import *
listA = [1,2,3,4,5]
listA = reduce(lambda x,y:x*y,listA,1)
print(listA)

# A decorator is a function that accepts a function as parameter and returns a function
def decor(fun):
    # writing the function which will be returned
    def inner():
        value = fun() # 10
        return value + 2 #12
    return inner

@decor
def num():
    return 10
print(num())

def decorB(fun):
    def inner():
        value = fun()
        value = value * 2
        return value
    return inner

@decorB
def numB():
    return 10

print(numB())

# program 3
def decor(fun):
    def inner():
        val = fun()
        return val + 2
    return inner

def decor1(fun):
    def inner():
        value = fun()
        return value * 2
    return inner

@decor1
@decor
def numC():
    return 10

print(numC())