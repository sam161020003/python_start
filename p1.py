a='samarth'
d=True    #T should be capital
f=4+5j   # i ki jagah j hoga
print (a)
print(f.real)
print(f.imag)
print(type(a)) # type() tells about type of data type
print(type(d))
print(type(f))

# TO EXTRACT 
print(a[4])

# LIST
l=[1,2.3,True,4+5j]
print(type(l))
print(l[-2]) # backward indexing
print(l[3])  #forward inedexing

# concept of slicing

s="kalash adhikari"
print(s[0:6])
print(s[0:15:2])  # third colon number is for how much is the jump if not 
# written it is automatically +1

#or
print(s[::2])
#or
print(s[0::2])

# To print in  reverse manner
print(s[::-1])

print(s[2:7:-1])    # nothing will be printed

print(s[15:0:-1])  # all in reverse except k letter