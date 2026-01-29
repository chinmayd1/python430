
#  CRUD 
#         0      1       2       3
names = ["ram","sham","sachin","rahul"]
print(names)
#retrive 
print(names[1])
#update 
names[1] = "ram"

#add
names.append("amol")
names.insert(2,"chinmay")

#delete
names.pop()
names.pop(1)
names.remove("ram")

# any value exist ?
print("rahul" in names)

# del min max ?
numbers = [11,22,33]

e = min(numbers)
e2 = max(numbers)
del numbers

# does list stores the value by index ?

# loop 
#            0          1        2       3
country = ["india","srilanka","china","pakistan"]
for x in range(4):
    print(x)
    print(country[x])

# for each 
for x in country:
    print(x)

# while loop 

i = 0
while(i < len(country)):
    print(country[i])
    i = i + 1


# methods 

numbers = [11,22,33,44,55]


numbers.append(66)
numbers.pop()
numbers.remove(11)
numbers.extend([122,22,333,444])
numbers.sort()
numbers.reverse()
numbers.clear()
numbers.copy()
numbers.insert(3,333)
numbers.index(2)

d = [11,22,33]
e  = d.copy()
e[1] = 222
print(d)
print(e)





