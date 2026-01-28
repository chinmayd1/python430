

text = "hello python"
e1= text.lower()  
e2 = text.upper()

# strip 
text2 = " goa "
print(len(text2))
text2 = " goa "
e3 = text2.strip()
print(e3)
print(len(e3))

text3 = " goa "
print(len(text3))
e4 = text3.lstrip()
print(len(e4))

text4 = "goa "
print(len(text4))
text4 = "goa "
e5 = text4.rstrip()
print(len(e5))

text5 = "i  am learning python"
e6 = text5.replace("python","javascript")
print(e6)

text6 = "chinmaydeshpande010@gmail.com"
#["chinmaydeshpande010","gmail.com"]
e7 = text6.split("@")
print(e7)

e8 = "@".join(e7)
print(e8)

text7 = "aachal"
e9 = text7.split("c")
print(e9)
e10 = "c".join(e9)
print(e10)

# 0   1   2   3   4   5   6
# c   h   i   n   m   a   y
text8 = "chinmay"
e11 = text8.find("a")
print(e11)

text9 = "aachal"
e12 = text9.count('a')
print(e12)

text10 = "aachal"
e13 = text10.startswith("aa")
print(e13)

e14 = text10.endswith('al')
print(e14)


text11 = "aachal"
print(text11.isalpha())
print(text11.isdigit())
print(text11.isalpha())
print(text11.isspace)
print(text11.isdecimal())

e15 = "hello-python-world".partition("-")
print(e15)
e15 = "hello-python-world".rpartition("-")
print(e15)

e16  ="unhappy"
e16 = e16.removeprefix("un")
e17 = "file.txt".removesuffix(".txt")
print(e17)

e17 = "CHINMAY"
e2 = e17.capitalize()
print(e2)

text11 = "Chinmay is learning"
e19 = text11.title()
print(e19)

e20  = e19.istitle()
print(e20)

text12 = "555" 
e21 = text12.zfill(5)
print(e21)


# my name is chinmay and lastname is deshpande

fn = "chinmay"
ln = "deshpande"
print("my name is {} and lastname is {}".format(fn,ln))
print(f'my name is {fn} and lastname is {ln}')


