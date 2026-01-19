
#          fn         ln      ag  rollno
info = ["chinmay","deshpande",34,56]
# dict
dictA = {
    # prop:value
    # key:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":56
}
print(dictA)

# does dictionary stores the value by index ? - No

dictA = {
    # prop:value
    # key:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":56
}
#print(dictA[0])

# Does dictionary allow to store duplicate values? - No
listA = [11,22,33,11,22]
print(listA)
dictA = {
    # prop:value
    # key:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":56,
    "firstName":"sarika"
}
print(dictA)

# particular key exist in dictionary ??
dictA = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":56,
    "firstName":"sarika"
}
print(dictA)
listA = [11,22,33,11,22]
print(33 in listA)
print("firstName" in dictA)
print("rollNo" in dictA)
print("Age" in dictA)

# program 2

names = ["sarika","poorva","mayuri","ram"]
e = len(names)
print(e)

vehicle = {
    "color":"red",
    "type":"sedane",
    "regNo":123
}
print(vehicle)
print(len(vehicle))
# deleting the dictionary 
#del vehicle

# methods in dictionary
# retrive

listA =[11,22,33]
print(listA[0])

vehicle = {
    "color":"red",
    "type":"sedane",
    "regNo":123
}
print(vehicle['color'])
print(vehicle['type'])
print(vehicle['regNo'])
e2 = vehicle.get('color')
print(e2)

# updating the value from dictionary

vehicle = {
    "color":"red",
    "type":"sedane",
    "regNo":123
}
print(vehicle['color'])
vehicle['color'] = "blue"
print(vehicle)

# add the property and valu to dictionary
vehicle['model'] = "Q4"
print(vehicle)

# deleting the property
vehicle.pop('model')
print(vehicle)

# C R U D