
info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "skills":["python","javascript","sql","html"],
    "age":34
}
print(type(info))
print(len(info))
print("firstName" in info)
print(info)

# program 2
# info = {
#     "firstName":"chinmay",
#     "lastName":"deshpande",
#     "age":23,
#     "skills":["python","javascript","sql","html"],
#     "age":34
# }
# # retrive 
# print(info['firstName'])
# e = info.get('age')
# print(e)
# # update 
# info['firstName']  = "aachal"
# print(info)
# # add 
# info['city'] = "pune"
# # delete
# #del info
# info.pop('age')

# program 2
info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "skills":["python","javascript","sql","html"],
    "age":34
}
print(info['firstName'])
for x in info:
    print(x,info[x])

# program 3


info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "skills":["python","javascript","sql","html"],
    "age":34
}

for x in info.keys():
    print(x)

for x in info.values():
    print(x)

for x,y in info.items():
    print(x,y)


info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "skills":["python","javascript","sql","html"],
    "age":34
}

# info.popitem()
# info.pop('age')
# del info['skills']

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "skills":["python","javascript","sql","html"],
    "age":34
}

info.update({'language':"marathi"})
print(info)

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "skills":["python","javascript","sql","html"],
}
e = info.setdefault('age',44)
print(e)
info.clear()
print(info)

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "skills":["python","javascript","sql","html"],
}
# info2 = info
# info2['age'] = 44
# print(info)
# print(info2)

info2 = info.copy()
info['age'] = 44
print(info2)
print(info)

e = dict.fromkeys(["one","two","three"],0)
print(e)