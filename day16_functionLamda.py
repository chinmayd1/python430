add  = lambda x : x + x
e = add(1)
print(e)

# function as a parameter 
def addition(fn,x):
    #fn = lambda x : x + x
    # x  = 10
    e = fn(x) 
    return e # function call
e2 = addition(add,10)
print(e2)

# function as a return type 
def subtraction():
    return lambda  x:x-x
subA = subtraction()
e4 = subA(5) # function call
print(e4)

# program 4

birthYear = [2000,2001,2002,2003]
ages = []
for x in birthYear:
    ages.append(2026 - x)
print(ages)
e = map(lambda x :2026 - x,birthYear)
print(list(e))

# program 5

numbers = [11,22,33,44,55]
e2 = map(lambda x : x + 10,numbers)
print(e2)
print(list(e2))


# program 6
marks = [99,34,55,66,77,88,44]
above60 = []
for x in marks:
    if x > 60:
        above60.append(x)
print(above60)



e5 = filter(lambda x : x > 60,marks)
e6 = list(e5)
print(e6)
transactions = [43,55,66,3,-45,60,-33,55,66]
deposit =  list(filter(lambda x: x > 0,transactions))
print(deposit)

withdrawl =  list(filter(lambda x: x < 0,transactions))
print(withdrawl)


# program 1
numbers = [11,22,33]
total = 0

for x in numbers:
    total = total + x
print(total)

from functools import reduce 
numbers = [11,22,33]
e = reduce(lambda acc,x:acc+x,numbers,0)
print(e)

# list comprehension ----> output ----> list ---> []
#[expression:loop:conditio]

# program 2
numbers = [1,2,3,4,5,6,7,8,9,10]
#[2,4,6,8,10,12,14,16,18,20]
e  = [x * 2 for x in numbers]
print(e)

marks = [44,55,22,11,66,33,44,55,66]
above30 = []
for x in marks :
    if x > 40:
        above30.append(x)
print(above30)

above302  = list(filter(lambda x : x > 40,marks))
print(above302)

#[expression:loop:condition]
above303 = [x for x in marks if x > 40]
print(above303)

# program 3

names = ["chinmay","sarika","ram","aachal"]
e = list(map(lambda x:x.upper(),names))
print(e)

e2 = [x.upper() for x in names]
print(e2)

# program 4
transactions = [11,-12,120,-13]
deposit =list(filter(lambda x : x > 0,transactions))
print(deposit)

withdrawls =list(filter(lambda x : x < 0,transactions))
print(withdrawls)

# program 5

numbers = [11,22,33,44]
print([x for x in numbers if x % 2 == 0])
#["odd","even","odd","even"]

print(["even" for x in numbers if x % 2 == 0])

#[tenary operator:loop]
e3 =["even" if x % 2 == 0 else "odd" for x in numbers]
print(e3)