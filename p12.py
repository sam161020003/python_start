#SET  has no indexing operation nor slicing operation
s={2,3,5,6}
print(type(s))
# it removes all the suplicate data items and it ascending order but not always
s1={2,23,2,23,4,1,3,4,221}
l=list(set(s1))
print(l)
print(s.add("sa"))
print(s.remove("sa"))
