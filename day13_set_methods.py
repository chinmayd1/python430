
setA = {11,22,33}
setB = {22,33,44}
print(setA.union(setB))


setA = {11,22,33}
setB = {22,33,44}
print(setA.intersection(setB))
setA.intersection_update(setB)
print(setA)

setA = {11,22,33}
setB = {22,33,44}
print(setA.difference(setB))
setA.difference_update(setB)
print(setA)


setA = {11,22,33,44}
setB = {22,55,66}

print(setA.symmetric_difference(setB))

setH = {11,22,33}
setG = {33,44,55}

print(setH.symmetric_difference(setG))
setG.symmetric_difference_update(setH)
print(setG)


setT ={11,33,44}
setN = {55,66,77}
print(setT.isdisjoint(setN))


setT ={11,33,44}
setN = {55,66,77}


setA = {11,22,33}
setB  = {11,22}
print(setB.issubset(setA))
print(setA.issuperset(setB))


setA = {11,22,33}
setB  = {11,22}

setA.update({66,77,88,99})
setA.add()
setA.clear()
setE = setA.copy()
setE.pop()
setE.remove(77)

# int , float  , boolean , list , dict , str , tuple , set 
# function
# sql 