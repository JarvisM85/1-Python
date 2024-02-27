########################################################
# DATE ==> 01/08/2023

# use if ZIP Function

name = ['dada','mama','kaka']
info = [9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)

# use of zip function with mis match list
name = ['dada','mama','kaka','baba']
info = [9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)

# but the disadvantage is that 
#avoids the excess elements ==>  solution is zip_longest
#-------------
## zip longest
from itertools import zip_longest
name = ['dada','mama','kaka','baba']
info = [9850,6032,9785]
for nm,inf in zip_longest(name,info):
    print(nm,inf)

#######
# use of fill value instead of None
# It will avoid print None in Output but fillvalue


from itertools import zip_longest
name = ['dada','mama','kaka','baba']
info = [9850,6032,9785]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)
    
#####
# use of all() if all the values are TRUE then
# --------------
# it will produce output
lst = [2,3,-6,8,5]
if all(lst):
    print('all values are true')
else:
    print('Useless')
    
lst = [2,3,-6,0,5]
if all(lst):
    print('all values are true')
else:
    print('Useless')
############
# use of any if any one is positive
#     ==================
lst = [0,0,0,9,0]
if any(lst):
    print('some value is present')
else:
    print('Useless')

lst = [0,0,0,-2,0]
if any(lst):
    print('some value is present')
else:
    print('Useless')

lst = [0,0,0,0,0]
if any(lst):
    print('some value is present')
else:
    print('Useless')
#####################################
# count() --> itertool used to count
from itertools import count
counter = count()
print(next(counter))
print(next(counter))
print(next(counter))

# Now lets Start from 1
from itertools import count
counter = count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))

#####################
# cycle() ==> suppose you have repeated tasks to be done
#then you can use this method
import itertools
instructions = ("Eat","code","sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)

########################
#repeat()
from itertools import repeat
for msg in repeat("keep patience",times=3):
    print(msg)

#########################################
'''
#Permutation=> arrangemnet
#Combinations=> selection
'''
#combinations()
from itertools import combinations
players = ['John','Jani','Janardhan']
for i in combinations(players,2):
    print(i)

#permutation()
from itertools import permutations
players = ['John','Jani','Janardhan']
for seat in permutations(players,2):
    print(seat)
    
#######################
# product()
from itertools import product
team_a = ['Rohit','Pandya','Bumrah']
team_b = ['Virat','Manish','Shami']
for pair in product(team_a,team_b):
    print(pair)

###################################################
###################################################
'''
# AFTERNOON :==>
**************************
'''
# filter()
age = [27,17,21,19]
adults = filter(lambda age:age>=18,age)
print([age for age in adults])
#################################################
'''
10/10 times
imp==> 
Shallow copies==>
Deep copies ==>

'''
#Assignment operation
#This will only create a new variable with the same reference.
#Modifying
list_a = [1,2,3,4,5]
list_b = list_a

list_a[0]=-10
print(list_a)
print(list_b)
#########
## Shallow Copy ==>  for 1 level 

import copy
list_a = [1,2,3,4,5]
list_b = copy.copy(list_a)
# does not affects the other list
list_b[0] = -10
print(list_a)
print(list_b)

#########
#But for nested objects ,modifying on level 2 or
# deeper does affect the other list
import copy
list_a = [[1,2,3,4,5],[5,6,7,8,9,10]]
list_b = copy.copy(list_a)
# it does affect the other list
list_a[0][0] = -10
print(list_a)
print(list_b)

###########################################################
#3 # DEEP Copies==>
#Full independent clones=> use copy.deepcopy()
#                         =========================

import copy
list_a = [[1,2,3,4,5],[5,6,7,8,9,10]]
list_b = copy.deepcopy(list_a)
# it does NOT affect the other list
list_a[0][0] = -10
print(list_a)
print(list_b)









