
listA = [11,22,33]
e = listA.append(44)
print(e)
print(listA)

# program 2
names = ["chinmay","sarika","ram","sham"]
names.pop()
print(names)
names.pop(1)
print(names)

# program 3
animals = ["tiger","lion","panthar","snake"]
animals.remove("tiger")
print(animals)

# program 4
listA = [11,22,33]
listB = [22,33,444]

# listA.extend(listB)
# print(listA)
listB.extend(listA)
print(listB)

# program 5
cities = ["pune","mumbai","bangalore","kolkata"]
print(cities)
cities.insert(2,"nagpur")
print(cities)


cities = ["pune","mumbai","bangalore","kolkata","pune","wardha","chennai","pune"]
e = cities.index("pune")
e2 = cities.index("pune",2)
e3 = cities.index("pune",2,5)
print(e)
print(e2)
print(e3)

cities = ["pune","mumbai","bangalore","kolkata","pune","wardha","chennai","pune"]
cities.sort()
print(cities)

country = ["india","pakistan","srilanka"]
country.reverse()
print(country)

number = [22,33,44,23,44,22,33,44,22]
e4 = number.count(22)
print(e4)


number = [22,33,44,23,44,22,33,44,22]
number.clear()

a = [11,22,33]
b = a
# print(a)
# print(b)
# b.append(44)

# print(a)
# print(b)

c = a.copy()
c.append(44)
print(a)
print(c)