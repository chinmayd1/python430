str = "chinmay"
e = str.upper()
print(e)

str2 = "Poorva"
f = str2.lower()
print(f)

str3 = "kanchan"
g = str3.capitalize()
print(g)

str4 = "i am learning python"
h = str4.title()
print(h)

# program 2
# checked methods - boolean 

s1 = "CHINMAY"
print(s1.isupper())

s2 = "poorva"
print(s2.islower())

s3 = "I Am Learning Javascript"
print(s3.istitle())

s4 = "aachal"
print(s4.startswith("a"))
print(s4.startswith("aa"))

s5 = "ninad"
print(s5.endswith("d"))
print(s5.endswith("nad"))

s6 = "0123213"
print(s6.isdigit())

s7 = "ram11"
print(s7.isalpha())

s8 = "123321DAS"
print(s8.isalnum())# alphats , numbers , alphanumber

s9 = " "
print(s9.isspace())