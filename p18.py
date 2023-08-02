l1=[1,2,3,4,"sam",[5,6,7]]
def op(k):
    l=[]
    for i in k:
        if  type(i)==list:
            for j in i:
                l.append(j)
        else:
            if type(i)==int:
                l.append(i)
    print(l)   

op(l1)