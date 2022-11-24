#Write a python script to check if a string contains only numbers.
# Initialising string
a = '1234556'
 
# printing initial string
print ("Initial String : ", a)
 
digits="0123456789"
c=0
for i in a:
    if i in digits:
        c+=1
if len(a)==c:
    print ("string contains all numbers")
else:
    print ("string doesn't contains all numbers")