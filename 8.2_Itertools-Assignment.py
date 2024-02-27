# DATE ==> 01/08/2023

#         Itertools Assignments ==>
#        ****************************
'''
1. Write a python program to create an iterator
from several iterables in a sequence and display
the type and elements of the new iterator.
'''
# -> for LIST
from itertools import chain
def chain_func(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
#List
result = chain_func([1,2,3],['a','b','c','d'],[4,5,6,7,8,9])
print("Type of the new iterator :")
print(type(result))
print("Elements of the new iterator :")
for i in result:
    print(i,end=' ')

# for TUPLE
from itertools import chain
def chain_func(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
#Tuple
result = chain_func((10,20,30,40),('A','B','C','D'),(40,50,60,70,80,90))
print("Type of the new iterator :")
print(type(result))
print("Elements of the new iterator :")
for i in result:
    print(i)
################################################   
'''
2. Write a python program that generates the running
product of elements in an iterable.
'''
# For List
from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)
#LIST
result = running_product([1,2,3,4,5,6,7])
print("Running product of a list :")
for i in result:
    print(i)
######    
# For Tuple-->
from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)
#Tuple
result = running_product((1,2,3,4,5,6,7))
print("Running product of a tuple :")
for i in result:
    print(i)
################################################   
'''
3. Write a python program to construct an infinite inerator that
returns evenly spaced values starting with a 
specified number and step.
'''
import itertools as it
start = 10
step = 1
print("The Starting number is ",start,"and step is",step)
my_counter = it.count(start,step)
#following loop will run for ever
print("The said function print never-ending items :")
for i in my_counter:
    print(i)

################################################   
'''
4. Write a python program to generate an infinite
cycle of elements from an iterable .
'''
import itertools as it
def cycle_data(iter):
    return it.cycle(iter)
#following loops will run for ever
#LIST
result = cycle_data(['A','B','C','D'])
print("The said Function print never-ending items :")
for i in result:
    print(i)
    
    
#String
result = cycle_data('Python itertools')
print("The said Function print never-ending items :")
for i in result:
    print(i)

################################################   
'''
5. Write a python program to make an iterator
that drops elements from the iterable as soon as an 
element is a positive number .
'''
import itertools as it
def drop_while(nums):
    return it.dropwhile(lambda x:x < 0,nums)
nums = [-1,-2,-3,8,4,-10,2,0,5,12]
result = drop_while(nums)
print("Drops elements from the iterable when a positive number arises : \n",list(result))

#Alternate solution
def negative_num(nums):
 
    
    






















































