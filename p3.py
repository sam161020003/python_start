# arithmetic opertaors
j=4
print(j**3) #power

a=79
print(a//7) #floor

# comparison operator
print(1<2)
print(1!=2)
print(1==2)
print(1<=2)

# logical operators

print(True and True)
print(True or True)
print(False and  True)
print(1  and 0)
print(not True)
print(not 0)  # answer true ya false mein hi aayega 1 and nhi

#bitwise operator converts everyting to binary

print(10 & 4)
print(23 & 20)
print(23 | 20)  

# bin function converts every number to binary 
# see the technique of how to find answer of line 26(jahaan nhi hai vahan 0 daal do)
# similarly or operation
print(bin(2234))
print(bin(23))
print(bin(20))

# binary not
print(bin(~12))
print(bin(-13))   # as ~12= -13 hota hai
# iske liye pehle 12 ko convert kro binary mein phir saare digits reverse kro

# right and left shift operator

z=8   
b= z>>3   # right shift operator
print (b)