name = ['dada','mama','kaka']
info = [2623,7985,4623]
for nm,inf in zip(name,info):
    print(nm,inf)



from itertools import zip_longest    
name = ['dada','mama','kaka','baba']
info = [2623,7985,4623]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)
    
###################################################
lst = [1,3,-46,+8,-5,2]
if all(lst):
    print("Valid")
else:
    print("Invalid")
    #all()
    #ant()

lst = [0,0,0,0,0]
if any(lst):
    print("Valid")
else:
    print("Invalid")

#####################33
from itertools import count
counter = count(start=100)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

###############
#cycle
import itertools
tasks = ["Eat","Code","Sleep"]
for task in itertools.cycle(tasks):
    print(task)



#repeat
from itertools import repeat
for msg in repeat("hello students",times =4):
    print(msg)

#################################################3
from itertools import combinations
players = ['john','jani','jerry']
for i in combinations(players, 2):
    print(i)
    
from itertools import permutations
players = ['john','jani','jerry']
for i in permutations(players,2):
    print(i)


from itertools import product
a = ['Rohit','Hardik','Dhoni']
b = ['Virat','Surya','Ishan']
for i in product(a,b):
    print(i)

#######
#filter 

age = [27,17,21,19]
adult = filter(lambda age:age>=18,age)
#print(list(adult))
print([age for age in adult])

age = [52,12,3,5,14,36,12,45,8]
adult = filter(lambda age : age >=20 ,age)
print(list(adult))


##################################
a = [1,2,3,4,5]
b = a

a[0]=-10
print(a)
print(b)


#shallow copy
import copy
a = [1,2,3,4,5]
b = copy.copy(a)

a[0]=-10
print(a)
print(b)


#does not support 2 level 
import copy
a = [[1,2,3,4,5],[6,7,8,9,10]]
b = copy.copy(a)

a[0][0]=-10
print(a)
print(b)


#deep copy
import copy
a = [[1,2,3,4,5],[6,7,8,9,10]]
b = copy.deepcopy(a)

a[0][0]=-10
print(a)
print(b)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

name = ['dada','mama','kaka']
info = [9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)

from itertools import zip_longest
name = ['dada','mama','kaka','baba']
info = [9850,6032,9785]
for nm,inf in zip_longest(name,info):
    print(nm,inf)


from itertools import zip_longest
name = ['dada','mama','kaka','baba']
info = [9850,6032,9785]
for n,i in zip_longest(name,info,fillvalue=0):
    print(n,i)


lst = [2,63,46,3,0,6]
if all(lst):
    print(True)
else:
    print("Useless")


lst = [0,0,0,0,0,0]
if any(lst):
    print(True)
else:
    print("Useless")

from itertools import count
counter = count(start=10,step=3)
print(next(counter))

    
import itertools
lst = ['eat','sleep','code']
for i in itertools.cycle(lst):
    print(i)
    
from itertools import cycle
lst = ['eat','sleep','code']
for i in cycle(lst):
    print(i)

from itertools import repeat
for i in repeat("Code eat and Sleep",times=3):
    print(i)
    
    
import itertools 
for i in itertools.repeat("Code eat and Sleep",times=3):
    print(i)
    
from itertools import permutations
players = ['dada','mama','kaka']
for i in permutations(players,2):
    print(i)
    
    
from itertools import combinations
players = ['dada','mama','kaka']
for i in combinations(players, 2):
    print(i)
 
from itertools import product
a = ['dada','mama','kaka']
b = ['sahil','abhi','akash']
for i in product(a,b):
    print(i)
    
age = [25,2,42,12,3,62,17,5]
adults = filter(lambda age:age >18,age)
print([age for age in adults])
   

age = [25,2,42,12,3,62,17,5]
lst = [a for a in age if a>=18]
print(lst)


age = [25,2,42,12,3,62,17,5]
adults = filter(lambda x : x >=18,age)
print([a for a in adults])



list_a = [1,2,3,4,5]
list_b = list_a
list_a[0]=-10
print(list_a)
print(list_b)


import copy
list_a = [1,2,3,4,5]
list_b = copy.copy(list_a)
list_a[0]=-10
print(list_a)
print(list_b)

import copy
list_a = [[1,2,3,4,5],[10,20,30,40,50]]
list_b = copy.deepcopy(list_a)
list_a[0][0]= -99
print(list_a)
print(list_b)

'''
#@@@@@@@@@@@  Assignment    @@@@@@@@@@@@@#
            --------------
'''
from itertools import chain
def chain_fun(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
result = chain_fun([1,2,3],['a','b','c','d'],[23,568,95])
print(type(result))
for i in result:
    print(i,end=' ')
    
    
from itertools import chain
def chain_fun(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
result = chain_fun((1,2,3),('a','b','c','d'),(23,568,95))
print(type(result))
for i in result:
    print(i,end=' ')
        
############################################
from itertools import accumulate
import operator

def run_pt(lst):
    return accumulate(lst,operator.mul)
lst = run_pt([1,2,3,4,5,6,7])    
for i in lst:
    print(i)
    
    

