# program 1
for x in range(1, 11):
   if  x == 5:
      continue
   print(x)
   #print("Hello World")

# program 2
i1 = 1
while(i1 <= 5):
   if i1 == 3:
      i1  =  i1 + 1 #4
      continue
   print(i1) #1 #2 #4 # 6
   i1 += 1 #2 #3 #5 #6

#          0  1  2  3  4
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(type(numbers))

#names list
#           0          1          2        3
names = ["chinmay", "sachin", "vaibhav", "amol"]
print(names)
print(type(names))

# mixed list
info  = [1, 7709192441,"chinmay","deshpane" ,True]
print(info)
print(type(info))

# total number of elements in the list
print(len(numbers))
print(len(names))
w = len(info)
print(w)

# access elements from the list using index - yes
#          0  1  2  3 
numberB = [11,22,33,44]
print(numberB[0])
print(numberB[1])  
print(numberB[2]) 

# updating the value 
print(numberB[0])
numberB[0] = 111
print(numberB)



list1 = [10,20,30,40,50]

