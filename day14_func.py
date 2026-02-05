# a = 10
# b = 15
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)

# c = 8
# d = 4

# print(c+d)
# print(c-d)
# print(c*d)
# print(c/d)
# print(c%d)

# def Calculator(x,y):
#     print(x+y)
#     print(x-y)
#     print(x*y)
#     print(x/y)
#     print(x%y)
# Calculator(12,3)
# Calculator(12,3)

# function with out and without return type
# def CalA():
#     print(9+9)
# CalA()
# CalA()
# CalA()
# # function with parametr and without return type 
# def CalB(x,y):
#     print(x+y)

# CalB(23,4)
# CalB(23,1)
# CalB(23,3)

# # function with parameter and with return type 

# def Calc(x,y):
#     return x + y
# e2 = Calc(12,3)
# print(e2 + e2)

# default parameter
def CalD(x=8,y=4):
    print(x+y)
CalD()
CalD(12)
CalD(12,4)

# positional argument
# x = 10
# y = 5
def CalE(x,y):
    print(x-y)
CalE(y=5,x=10)

#args

# q = 1,2,3,4,5,6,7
# print(q)
def addAll(*args):
    print(args)
    return sum(args)
e = addAll(12,3,4,5,6,7,8,9,5,6,7,8,9,4,6)
print(e)

#**kwargs

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
}

def addCity(**kwargs):
    print(kwargs)
    info.update(kwargs)
    return info

updateD = addCity(city="pune",language="marathi")
print(updateD)


