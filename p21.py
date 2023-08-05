# using while loop
def test1():
    a,b=0,1
    while True:# hmesha chalega always true
        yield a # a ki intial value print kr rha hai
        a,b=b,a+b
fib=test1()
for i in range(10):
    print(next(fib))
    # generator hai mtlb iterator hai
#The next() function is used to retrieve the next value from the generator. When next(fib) is called, the generator function test1() is executed up to the yield statement, and it returns the current value of a. The generator then pauses its execution, preserving its internal state.
#The next time next(fib) is called, the generator resumes execution from where it left off and continues generating the Fibonacci sequence.