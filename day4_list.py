
listA = [11,22,33]
print(listA)

names = ["chinmay","shirsh","ram"]
print(names)
print(type(names))

info = ["chinmay",7709192441,True]
print(info)
print(type(info))


# CRUD
# Create
flowers = ["rose","jasmine","lotus"]

# Update
# Does the list stores the value by index 
#           0         1      2
animals = ["tiger","lion","rabbit"]
#            -3        -2       -1
print(animals[0])
print(animals[-1])
animals[0] = "snake"
print(animals)

# total elements in list
numbers = [11,22,33,44,55]
e = len(numbers)
print(e)

# del 
# del numbers
# print(numbers)
# particular element exist in list
#           0       1         2         3
cities = ["pune","mumbai","banglore","kolkata"]
print("Pune" in cities)

# loops 

# for range
#          0  1  2    3    4
numbers = [1,22,333,4444,55555]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

# startIndex - 0
# endIndex - 5(not included)
for x in range(len(numbers)):
    #print(x)
    print(numbers[x])

#          0        1        2       3
names = ["samay","poorva","aachal","sumit"]
for x in range(4):
    #print(x)
    print(names[x])

# for Each 
countries= ["india",'bangladesh',"srilanka","china"]
for x in countries:
    print(x)

# while loop
numbers = [11,22,33,44,55]
i1 = 0
while(i1 < len(numbers)):
    #print(i1)
    print(numbers[i1])
    i1 = i1 + 1