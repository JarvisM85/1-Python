# DATE --> 31/07/2023

# by normal method
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

# same code by LIST Comprehension ==>
#            ------------------------- 
lst=[num for num in range(0,20)]
print(lst)

####
names = ['dada','mama','kaka']
lst=[name.capitalize() for name in names]
print(lst)

#######
# list comprehension with IF Statement
def is_even(num):
    return num%2==0
lst = [num for num in range(20) if is_even(num)]
print(lst)
#######
# looping of for loop in list comprehension
lst = [f"{x}{y}" for x in range(3) for y in range(3) ]
print(lst)

########################################################
# Set Comprehension ==> 
set_a = {x for x in range (3)}
print(set_a)

################################################
# Dictionary Comprehension ==>
dict = {x:x*x for x in range (3)}
print(dict) 

################################################
#            Generator
#         ================
#It is another way of creating iterators
#in a simple way where
# it uses keyword "yield" --> function which returns multiple values
#               ===========
# insted of returning it in a defined function]
# Generators are implemented using a function

gen = (x for x in range(3))
print(gen)  # ====> Object is Created here
for num in gen:
    print(num)
    
###
#Another way of accesing values from Object in Generators
gen = (x for x in range(3))
next(gen)
next(gen)
next(gen)

###############################################
# Function Which return Multiple Values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)

###
# Now instead of using for loop we can write our 
# own generator
gen = range_even(6)
next(gen)
next(gen)
#################################
#Changing Operators 
def lengths (itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
passwords = ["good-man","give'm-pass","00100=100"]
for password in hide(lengths(passwords)):
    print(password)


###
def lengths (itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
import string
adjectives=['sleepy','slow','smelly','wet','fat','red','orange','yellow','green']
nouns=['apple','dinosaur','ball','toaster','goat','dragon','hammer','duck','panda']
import random
adjectives=random.choice(adjectives)
nouns=random.choice(nouns)
number = random.randrange(0,100)
special_char = random.choice(string.punctuation)
passwords = adjectives + nouns + special_char + str(number)
print(passwords)
for password in hide(lengths(passwords)):
    print(password,end='')


##############################################
#           Enumerate
###       =============      #####
# printing list with index
# without using enumerate--> normal
lst = ["milk","eggs","Bread"]
for index in range (len(lst)):
    print(f"{index+1} {lst[index]}")
###
# With using enumerate-->
lst = ["milk","eggs","Bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item} ")
    
####################################################33
#####--------------------------------------------######
####---------------------------------------------####


s = "Hello 123 my name is 35 and my prof is 3738"
w = s.split()
print(w)
r = [n for n in w if not n.isalpha()]
print(r)

















