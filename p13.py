# dictionary data type 
# key should always be unique othewise it updates itself see d2
# general syntax d={'key':'value'}
# no special case characters unless it is under quotes

d0={'name':'samarth','number':'102203303','email':'sadhkari'}
d1={234:'kalash',True:'good boy'}

#to access values
print(d0['name'])
print(d1[True]) # or print(d[1])

d2={'name':'samarth','ndcoinw':'nowno','name':"kalash"}
print(d2['name'])

# value can also be a list,tuple,set
d3={'falwa':'eai','fav':['hj','rr','kj']}
print(d3['fav'][2]) 

#dict in another dict is also allowed
# To add another key in one dictionary 
d3['faltu']=['mame','wfoi','wefo']
d3['ekb']=90
print(d3)

# to delete an element
del d3['falwa']
print(d3)

# see funciions of dict by d3.
d={'name':'nwojnd','fjjwe':'onwfwoenf','rollno':{'name':'samarth','number':'102203303','email':'sadhkari'}}
# now to access 102203303
print(d['rollno']['number'])

# giving list OR TUPLE OR SET (only change list in print)
#  of all keys or value in a dict
print(list(d.keys()))
print(list(d.values()))

# list of tuples holding key value pair
print(d.items())

#pop requires key and then it removes the corressponding value
print(d.pop('name'))