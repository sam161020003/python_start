from functools import reduce
l=[1,2,3,4,5]
# summation of all elememst in the list
print(reduce(lambda x,y:x+y,l))
# highest number
print(reduce(lambda x,y:x if x>y else y,l))

#CONDTIONS
# or we can use external function same as in mapping
# always two parameters in this x and y 
# no three parameters in reduce fucntion