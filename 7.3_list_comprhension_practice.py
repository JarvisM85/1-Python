lst = []
for num in range(0,20):
    lst.append(num)
print(lst)

lst = [num for num in range(20)]
print(lst)

names = ['DADA','maMa','kaKa']
lst = [name.capitalize() for name in names]
print(lst)
names = ['dada','mama','kaka']
lst = [name.upper() for name in names]
print(lst)
################################
def is_even(num):
    return num%2==0
lst = [num for num in range(20) if is_even(num)]
print(lst)




a = [5,6,3,4,8,9]
lst = [x for x in a if x is min(a) ]
print(lst)

lst = [5,6,3,121,52,68,99,4,9]
b = [num for num in lst if num==num[::-1]]
print(b)



a = input("Enter :")
if (a==a[::-1]):
    print("Palindrome")
else:
    print("NOT")


lst  = ['even' if num%2==0 else 'odd' for num in range(20)]
print(lst)

########################
lst = [f"{x}{y}"for x in range(3) for y in range(3)]
print(lst)

se = {x for x in range(5)}
print(se)

dict = {x:x**8 for x in range(4)}
print(dict)

#####################
# generators
gen = [x for x in range(3)]
print(gen)

gen = (x for x in range(4))
print(gen)
for i in gen:
    print(i)
    
gen = (x for x in range(3))
print(next(gen))
print(next(gen))
print(next(gen))


#############  
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(20):
    print(num)
##
def range_even(end):
    for num in range(0,end,2):
        yield num
gen = range_even(20)
print(next(gen))
################################

def length(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
passwords = ["good-man","happy_;student","excellent_boy","46546=65"]
for password in hide(length(passwords)):
    print(password)


#############################
#Enumerate
lst = ["milk","eggs","Bread"]
for i in range(len(lst)):
    print(f"{i+1} {lst[i]}")
    
lst = ["milk","eggs","Bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")
##############################
sentence = 'In 1984 there were 12 instances of a protest with 1000 attending'
words = sentence.split()
result = [num for num in words if not num.isalpha()]
print(result)


color = ['Red','Green','White','Black','Pink','Yellow']
color = [x for (i,x) in enumerate(color) if i not in(0,4,5)]
print(color)

###############################################
###############################################
###############################################
# DAte =>  13/08/2023

lst = []
for i in range(2,20):
    lst.append(i)
print(lst)


lst1 = [num for num in range(1,10)]
print(lst1)

names = ['dada','mama','kaka']
lst = [name.capitalize() for name in names]
print(lst)

lst1 = [name.lower() for name in names]
lst1

lst2 = [name.upper() for name in names]
lst2
#################
''' for list comprehension
for only if statement ==> LHS=business logic & RHS=if condition
for else condition --> lHS=condition & RHS=business logic
'''
def even_num(num):
    return num%2==0
lst = [num for num in range(20) if even_num(num)]
lst

def max_num(num):
    return max(num)
a = [52,636,163,5632,633]
print(max_num(a))


def even_num(num):
    return num % 2==0
lst = [num for num in range(0,20) if even_num(num)]
print(lst)

lst1 = [num for num in range(20) if num%2==0]
print(lst1)

lst = ['even' if num%2==0 else 'odd' for num in range(10)]
lst


lst = [f"{x}{y}" for x in range(4) for y in range(2)]
lst

s1 = {x for x in range(4)}
s1
lst = list(s1)
lst

dic ={x:x**3 for x in range (10)}
print(dic)


lst2 = ["even" if num%2==0 else "odd" for num in range(20)]
print(lst2)

lst3 = [num if num%2==0 else 'Nan' for num in range (20)]
print(lst3)

lst4 =[num for num in range(20) if num%2==0]
lst5 = [num for num in range(20) if num%2 != 0]
print("lst4 :",lst4)
print("lst5 :",lst5)

lst = [f"{x*y}" for x in range(7) for y in range(8)]
print(lst)


set1 = {i for i in range(3,20,2)}
print(set1)

dic = {x:x**3 for x in range(10)}
dic


import pandas as pd
dic ={"roll":[25,45,56,12,35],
      "name":['rohan','sahil','sam','nishant','akash'],
      "Courses":['java','python','sql','php','spark']}
data = pd.DataFrame(dic)
data

data=data.sort_values(by='roll',ascending=True).reset_index(drop=True)


#############################################################
#######*********************************###############
###################################################3

#DATE => 18/08/2023

lst = [x for x in range(3)]
print(lst)

gen = (x for x in range(3))
print(gen)
for num in gen:
    print(num)


gen = (x for x in range(3))
print(next(gen))
print(next(gen))
print(next(gen))


def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(10):
    print(num)

def range_even(end):
    for num in range(0,end,2):
        yield num
gen = range_even(6)
print(next(gen))

def even_n(end):
    for num in range(0,end,2):
       yield num
for num in even_n(10):
    print(num)
##################
def length(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
passwords = ["good-man","give'm-pass","00100=100"]
for pw in hide(length(passwords)):
    print(pw)
    
#_--------------------------


def length(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
import string
a = ['sleepy','slow','smelly','wet','fat','red','orange','yellow','green']
b = ['apple','dinosaur','ball','toaster','goat','dragon','hammer','duck','panda']
import random
a = random.choice(a)
b = random.choice(b)
sc = random.choice(string.punctuation)
num = random.randrange(0,100)

pw = a + b + sc + str(num)
print(pw)
for i in hide(length(pw)):
    print(i,end='')
    


lst = ["milk","eggs","Bread"]
for i in range (len(lst)):
    print(f"{i+1} {lst[i]}")

lst = ["milk","eggs","Bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")


#=================


s = "Hello 123 my name is 35 and my prof is 3738"
w = s.split()
print(w)
r = [n for n in w if not n.isalpha()]
print(r)


a = ['apple','dinosaur','ball','toaster','goat','dragon','hammer','duck','panda']

b = [x for (i,x) in enumerate(a) if i not in (0,4,5)]
b

#####################################################

string = "Yellow Yaks like yelling and yawing and yesterday they yodled while eating yuky yams"
lst = [c for c in string if c not in ('a','e','i','o','u',' ')]
print(lst)



list_a = [1,2,3,4]
list_b = [2,3,4,5]
lst = [n for n in list_a if  n in list_b]
lst


sentence = 'In 1984 there were 12 instances of a protest with 1000 attending'
words = sentence.split()
lst = [i for i in words if not i.isalpha()]
lst

lst = ['even' if num%2==0 else 'odd' for num in range(20)]
print(lst)


op = []
for i in range(20):
    if i%2==0:
        op.append('even')
    else:
        op.append('odd')
print(op)


list_a = [1,2,3,4,5,6,7,8,9]
list_b = [2,7,1,12]
lst = [(a,b) for a in list_a for b in list_b if a==b]
print(lst)

sentence = 'On a summer day Ramnath sonar went swimming in the sun and his red skin stung'
words = sentence.split()
lst = [word for word in words if len(word)<4]
print(lst)


#0 4 5
color = ['Red','Green','White','Black','Pink','Yellow']
lst = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(lst)


def cube_num(num):
    for i in range(1,num+1):
        yield i**3
num = int(input("Enter the Number :"))

for num in cube_num(num):
    print(num)


