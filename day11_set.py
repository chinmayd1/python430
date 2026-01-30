setA = {11,22,33,44}
print(setA)
print(type(setA))

# does set allows you to store duplicate values 
setB = {11,22,33,44,55,44}
print(setB)

# does set stores the value by index ?-NO
setC = {11,22,33}
#setC = setC[0]
print(setC)

# how search a value exist in set ?
setF = {12,33,44,55}
print(12 in setF)

# total number of elements in set 
setG  = {33,44,55,6}
e = len(setG)
print(e)

# set min and max
setK = {22,33,44}
e = min(setK)
print(e)
f = max(setK)
print(f)

# loop - forEach 
setName = {"poorva","ram","sham","shraddha","ramesh"}
for x in setName:
    print(x)


# methods 
setA = {22,33,44,55}
setA.add(66)
print(setA)


setA = {22,33,44,55}
setA.clear()
print(setA)

setA = {11,32,43,54}
setB = setA
setB.add(77)
print(setB)
print(setA)


setA = {11,32,43,54}
setN = setA.copy()
setN.add(77)
print(setA)
print(setN)

# remove
setA = {11,32,43,54}
setA.remove(43)
print(setA)

setA = {11,32,43,54}
setA.pop()
print(setA)


setA = {11,22,33}
setB = {33,44,55}
setC = setA.union(setB)
print(setC)

setA = {11,22,33,55}
setB = {33,44,55}
setC = setA.intersection(setB)
print(setC)
print(setA)
print(setB)

setA = {11,22,33,55}
setB = {33,44,55}
# setA.intersection_update(setB)
# print(setA)
setB.intersection_update(setA)


setA = {11,22,33,55}
setB = {33,44,55}

# setC = setA.difference(setB)
# print(setC)
# setC = setB.difference(setA)
# print(setC)

# setA.difference_update(setB)
# print(setA)

setB.difference_update(setA)
print(setB)