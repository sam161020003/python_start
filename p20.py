#for i in range(10):
  #  print (i)
# iss mein memory consumption high hai so we use generation functions

#fibbonacci number usng generator function
def test(n):
    a,b=0,1
    for i in range(n):
        yield a # a ki intial value print kr rha hai
        a,b=b,a+b

for i in test(20):
    print(i)
#helps in utilizing memory management
