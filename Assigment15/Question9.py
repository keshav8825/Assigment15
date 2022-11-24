#Write a python script to check if a string contains only characters of the alphabet.

# Python code to demonstrate
# to find whether string contains
# only letters
 
# Initialising string
a = "ababababa"
 
print ("Initial String", a)
 
# Code to check whether string contains only number
if a.isalpha():
    print("String contains only letters")
else:
    print("String doesn't contains only letters")