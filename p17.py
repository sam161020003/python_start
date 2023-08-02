# to extract integer type from another list
l=[1,2,3,4,"sam",[5,6,7,7]]
def op(k):
    l1=[]
    for i in k:
        if type(i)==int:
            l1.append(i)

    print(l1)

(op(l))

