# program 1

birthYear = [2000,2001,2002,2003]
# [26,25,24,23]
ages = []
for x in birthYear:
    # print(x)# element
    # print(2026 - x) # age
    ages.append(2026 - x)

print(ages)

# program 2  
marks = [89,45,66,77,88,33,46,77]
above60 = []
for x in marks:
    if x > 60:
        above60.append(x)
print(above60)

# program 3
# sum of all element of list 
numbers = [11,22,33]
total = 0
for x in numbers:
    total = total  + x
             #0    +  11  ----> 11
             #11   +  22  ----> 33
             #33   +  33  ----> 66
print(total)

# program 4
cities  = ["mumbai","bangalore","chennai","kolkata"]
for x in cities:
    print("welcome "+x)


# lamba functions 
#fnName = lambda(keyword)parameterOne, parameterTwo:statement(return statement)
add = lambda x,y:x+y
e = add(12,3)
print(e)

square = lambda x:x*x
print(square(2))

# function as a parameter and function as a return type 
x = 10
print(x)

add = lambda x,y:x+y
print(add)
print(add(12,3))


# function as a parameter to another function
def addition(fn,x,y):
    # fn = lambda x,y:x+y
    # x = 10
    # = 5
    e = fn(x,y)
    return e #15

e2 = addition(add,10,5)
print(e2)

# function returning another function
def subtraction():
    return lambda x,y:x-y

sub = subtraction()
#sub = lambda x,y:x-y
e = sub(13,4)
print(e)