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