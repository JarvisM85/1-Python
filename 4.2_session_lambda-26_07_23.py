#DATE --> 26/07/2023
#Morning
#Returing a Dictionary
def build_person(first_name,last_name):
    person={'first':first_name,'last':last_name}
    return person
musician=build_person('Ram','Sarkar')
print(musician)


###########################################
#Passing a List
def greet_user(names):
    for name in names:
        msg = f"Hello, {name.title()}."
        print(msg)
usernames=['Aniket','Sahil','Prajwal','Abhi']
greet_user(usernames)

##############################################
#Passing an Arbitrary Number of Arguments :--->>
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green pepper','extra cheese')
make_pizza('sahil')

#######  using for loop  ##############
def make_pizza(*toppings):
    print("\nMaking pizza with following toppings :")
    for topping in toppings:
        print(f" -{topping}")
make_pizza('pepperoni')
make_pizza('mushrooms','green pepper','extra cheese')

####################################################
#Mixing positional and arbitrary arguments
def make_pizza(size,*toppings):
    print(f"\nMaking a {size}-inch pizza with following toppings :")
    for topping in toppings:
        print(f" -{topping}")
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green pepper','extra cheese')

####################################################
import pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(18,'mushrooms','green pepper','cheese')


###########################
#importing specific function
from pizza import make_pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(18,'mushrooms','green pepper','cheese')

#using as to Give a Functions an Alias
from pizza import make_pizza as mp
mp(16,'pepperoni')
mp(18,'mushrooms','green pepper','cheese')

##########################################
#Importing All Functions in a Module

from pizza import*
make_pizza(16,'pepperoni')
make_pizza(18,'mushrooms','green pepper','cheese')

#####################################
# Scope of Variable
#Wrong forma--> we need to initialize first
x=x+1
x=6
print(x)

#Correct
x=6 #1st initialize
x=x+1 #
print(x)

##################################################
##################################################
##################################################

# Lamda Function or anonymous Function
def add(a,b,c):
    sum=a+b+c
    return sum
print(add(4,5,6))
add=lambda a,b,c:a+b+c
add(4,5,6)

#####################
def mul(a,b,c):
    multi=a*b*c
    return multi
print(mul(4,5,6))
add=lambda a,b,c:a*b*c
add(4,5,6)
    
    
#####
val=lambda *args:sum(args)
val(1,2,3,5,6)
val(1,2,3,5,7,8,9)
###############
#Keyword Arguments 

def person(name,**data):#name--->positional argument
          #**date --> Keyword argument
          # then what is arbitraty aggumnet
   print(name)
   print(data)
person(name='Navin',age=28,place='Mumbai',mob_no=985060)

########## Using for loop ##########
def person(name,**data):
   print(name)
   for i,j in data.items():
       print(i,":",j)
person(name='Navin',age=28,place='Mumbai',mob_no=985060)

#############
val=lambda **data:sum(data.values())
val(a=2,b=6,c=7,d=10)

max=lambda a,b:x if (a>b)#-->Error
print(max(1,2))

max=lambda a,b:x if (a>b) else b #-->Correct
print(max(1,2))
print(max(8,10))

max=lambda a,b:x if (a>b) else b #-->Correct
print(max(1,2))
print(max(10,8))

#########################################
#Python Collection Types







