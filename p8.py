l=[1,345,45,"sudh",True,5+7j,345.456]

# to extract any part of data in list use slicing
print(l[3][0:4:2])
# to convert any thing in string use str()
print(str(l[4])[0:3])               # see sytax
# Second way
a=str(l[4])
print(a[0:3])  
print(l.append("samarth"))  
# or any data type can be added usind upend

# string can only add with string 
#list can nly add with list but we can with append

print(l*2)
l1=[234,"samrth",56345.6]
# notice extend difference with append
print(l1.extend("kalash"))
# only iterable type can be used in extend not like int etc 
# but if we want to extend int type so in this way
print(l1.extend([2,3,4,4.3]))
print(l+l1)

#list with in list

print(l.append(l1))
# to access data of added list in list

print(l[-1][1])




