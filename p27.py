#Filter 
# to filter even object 
l=[1,2,3,3,4,49,64]
print(list(filter(lambda x: x%2==0,l)))
print(tuple(filter(lambda x: x%2!=0,l)))
print(set(filter(lambda x: x%2==0,l)))