l2=['sa',12,3.14,22]
l3=[]
l4=[]
for i in l2:
    if type(i)==int or type(i)==float:
     l3.append(i)
    elif type(i)==str:
     l4.append(i)

print(l3)
print(l4)