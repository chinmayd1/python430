
a = 12
print(a)
print(type(a))

b = 12.5
print(b)
print(type(b))

c = True 
print(c)
print(type(c))

d = [11,22,33,44]
print(d)
print(type(d))

f = {
    "firstName":"chinmay",
    "lastName":"deshpande"
}
print(f)
print(type(f))

# string 


a = "python"
b = 'python'
c = """
    I am learning python
    and python is used for AI
"""
e = '''
    Python is very
    similar to javascript
'''

print(a)
print(b)
print(c)
print(e)

# does string stores the value by index ?

fn = "chinmay"
# 0   1   2   3   4   5   6
# c   h   i   n   m   a   y 
#-7  -6  -5  -4  -3  -2  -1
print(fn)
print(fn[0])
print(fn[-1])


# is string mutable ? - No
lst  = [11,22,33] # mutable
print(lst[0])
lst[0] = 111
print(lst)

# n = "sarika"
# n[0] = "r"
# print(n)

# particular character or sub-string exist in string
fruits = "apple mango banana orange chikoo grapes"
print("app" in fruits)
print("App" in fruits)

# total number of characters in string 
city = "chandrapur"
e = len(city)
print(e)

# loop through string 
#           0         1      2        3
cities = ["mumbai","pune","madras","nagpur"]
city = "nagpur"

# range()
#range(startIndex,endIndex(not included),stepSize)
for x in range(len(cities)):
    #print(x)
    print(cities[x])

for x in range(len(city)):
    #print(x)
    print(city[x])

# forEach 
cities = ["mumbai","pune","madras","nagpur"]
city = "nagpur"

for x in cities:
    print(x)

for x in city:
    print(x)

cities = ["mumbai","pune","madras","nagpur","mumbai","raipur","mumbai"]
for x in range(len(cities)):
    if cities[x] == "mumbai":
        print(x)


# while

cities = ["mumbai","pune","madras","nagpur"]
city = "nagpur"

i1 = 0
while(i1 < len(cities)):
    print(cities[i1])
    i1 = i1+ 1

i2 = 0
while(i2 < len(city)):
    print(city[i2])
    i2 = i2 + 1

