

# CRUD 
# Method 
# tuple 
#           0         1       2
names = ["chinmay","sarika","ram"]
names[0] = "satish"
print(names)

# first_name = "chinmay"
# first_name[0] = "t"


# how to define tuple 

a = (11,22)
print(a)
print(type(a))


b = 11,12
print(b)
print(type(b))

# does tuple stores the value by index ?? - Yes
q1 = (11,22,33,44,55)
print(q1[0])

# can we update a single value in tuple? - No
# q2 = (11,22,33,44,55)
# print(q2)
# q2[1] = 11


# total number of elements in tuple
names = ("chinmay","sarika","sham","ram","satish")
print(names)
print(len(names))

numbers = (11,22,33,44)
print(min(numbers))
print(max(numbers))
del numbers


# program 2 
# find particular element present in tuple
countries = ("india","srilanka","china","bangladesh")
print("india" in countries) # boolean

# program 3
tupA = (11,22,33,44)
# range()
for x in range(len(tupA)):
    #print(x)
    print(tupA[x])

# for each 
for x in tupA:
    print(x)

#while
a = 0
while(a < len(tupA)):
    print(tupA[a])
    a = a + 1

# tuple unpacking 

tupB = (11,22,33,44)
one = tupB[0]
two = tupB[1]
three = tupB[2]
four = tupB[3]

print(one)
print(two)
print(three)
print(four)

tupB = (11,22,33,44)
a,b,c,d = tupB
print(a)
print(b)
print(c)
print(d)

tupC = (11,22,33,44)
tupC = list(tupC)
tupC.append(55)
tupC = tuple(tupC)
print(tupC)

tupC = (11,22,33,44,55,44)
e = tupC.count(44)
print(e)

e2 = tupC.index(11)
print(e2)

# slicing 

city = "chandrapur"
#  0     1    2    3    4     5   6    7   8   9
#  c     h    a    n    d     r   a    p   u    r
# -10   -9   -8   -7   -6    -5  -4   -3  -2   -1
#city[statIndex:endIndex(not included):step]
# default step size is 1
print(city[1::])
print(city[1:6:])
print(city[:len(city):])
print(city[0:len(city):2])
print(city[::-1])
print(city[-10:5])
print(city[-10:-2])
print(city[1:-1])
print(city[-1:-3])