#MAPPING 
l1=[2,3,4,5,66,56]
def seq(l):
    return l*2
print(set(map(seq,l1)))
print(tuple(map(seq,l1)))
print(list(map(seq,l1)))

# combination with lambda 
l1=[1,2,3,356,45,49]
l2=[34,23,453,23,34,5]
print(list(map(lambda x,y:x+y,l1,l2)))

