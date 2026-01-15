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