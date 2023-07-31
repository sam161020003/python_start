# append and extend only add data to last position 
# insert is used to add data in given lication in list
l=[True,4+7j,3.14,34]
l.insert(2,"sa")
print(l)
# or
l.insert(3,[3,4,5])
print(l)

#to remove data from list 
l.pop(-1)  # inside bracket give the index of number you want to remove
print(l)

#by removing
l.remove(True) # it removes the element which is passed 
print(l)

l1=[12.23,34,True,[2,3,4],"samarth"]
# to remove list element 3 from another list
l1[3].remove(3)
print(l1)

#to remove some character of samarth it is not possible 
#to sort
l3=[23,23,1,45,20]
l3.sort()
print(l3)
# if we want to reverse it in descending order than
l3.sort(reverse=True)
print(l3)
# it aslo sorts in alphabetical order