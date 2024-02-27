#DATE ==> 26/07/2023


##Python Collection Types
tup1=(1,3,5,7)
print(f'tup1[0]:\t {tup1[0]}')
print('tup1[1]:\t', tup1[1])
print('tup1[2]:\t', tup1[2])
print('tup1[3]:\t', tup1[3])

#Tuples can hold different data types
tup2=(1,'John',True,-23.45)
print(tup2[2])

#Iterating over tuples==>
tup3=('apple','orange','plum','apple')
for x in tup3:
    print(x)
    
#tuple related Function
#1.Length
len(tup3)
#2.count how many times a specified value occured
tup3.count('apple')
#3.To check which value is at specific index
tup4=('apple','orange','plum','apple','apple')
print(tup4.index('apple'))
print(tup4.index('plum'))
#4.Checking if an element Exists in tuple
if 'orange' in tup4:
    print("YES present")
else:
    print("NOT present")

#NESTED Tuples:
tuple1=(1,3,5,7)
tuple2=('John','Denise','Phobe','Adam')
tuple3=(42,tuple1,tuple2,5.5)
print(tuple3)

###################################################
###################################################
#2: LISTS   #Mutable,[],Ordered,indexed

lst1=[1,43.5,True]
lst2=['apple','orange',31]
root_list=['John',lst1,lst2,'Denise']
print(root_list)

###########3####
#Accessing elements from a list
lst1=['John','Paul','George','Ringo']
print(lst1[-1])
print(lst1[0])
print(lst1[-2])
lst1[-3]

#############################################

lst1=['John','Paul','George','Ringo']
print('lst1[1]:',lst1[1])
print('lst1[-1]:',lst1[-1])
print('lst1[1:3]:',lst1[1:3])
print('lst1[:3]:',lst1[:3])
print('lst1[1:]:',lst1[1:])
print('lst1[0:3:1]:',lst1[0:3:1])

#######################
#Adding to a list
#append ---> adding at the end of the list
lst1=['John','Paul','George','Ringo']
lst1.append('Pete')
print('lst1:',lst1)
#extend -->to extend the string  
lst1.extend(['Albert','Bob'])
print(lst1)

##########
#inserting into a list--> using insert
a_list=['Adele','Madonna','Cher']
print(a_list)
a_list.insert(1,'Paloma')
print(a_list)

##########
# list Concatenation
lst1=[3,2,1]
lst2=[6,5,4]
lst3=lst1 + lst2
print(lst3)

#############
# Removing from a list
lst1=[3,2,1,5,2,6,2]
lst1.remove(2)
print(lst1)

lst1=[3,2,1,5,2,6,2]
lst1.remove(lst1[2])
print(lst1)


lst1=[3,2,1,5,2,6,2]
print(lst1.count(2))

#the POP() method
lst6=['Once','upon','a','time']
print(lst6)
print(lst6.pop(1))
print(lst6)

#length
lst1=[3,2,1,5,2,6,2]
print(len(lst1))



#########ASSIGNMENTS##############
#1. take random 5 number s in the list and find min and max in the list
  #using max,min function
lst1=[4,8,77,56,5]
print("Minimum Number is :",min(lst1))
print("Maximum Number is :",max(lst1))

 # using sorting 
lst1=[4,8,77,56,5]
lst1.sort()
print("Minimum Number is :",lst1[0])
print('Maximum Number is :',lst1[-1])

  #using for loop
def min_value(values):
    min = values[0]
    for i in values:
        if i < min:
            min = i
    return min 
def max_value(values):
    max = values[0]
    for i in values:
        if i > max:
            max = i
    return max
lst1=[4,8,77,56,5]
print("The Minimum Number is :",min_value(lst1))
print("The Maximum Number is :",max_value(lst1))
  

#2.take 5 strings and make it reverse
lst2=['Aniket','Sahil','Prajwal','Abhi','Mahesh']
print(lst2[::-1])

lst2=['Aniket','Sahil','Prajwal','Abhi','Mahesh']
lst2.reverse()
print(lst2)



#3.take 10 numbers in list ,write script to search for value#check for value is present or not
lst3=[21,35,47,65,59,72,61,49,96,85]
x=int(input("Enter Number :"))
if x in lst3:
    print("YES Present")
else:
    print("NOT present")

#4.take 10 numbers in list ,insert some duplicate,write script to find duplicates

    
lst4=[21,35,47,21,59,72,61,49,59,85]
unique=[]
duplicate=[]
for i in lst4:
    if i not in unique:
        unique.append(i)
    elif i not in duplicate:
        duplicate.append(i)        
print(duplicate)



lst4=[21,35,47,21,59,72,61,49,59,85]
duplicate=[]
for i in lst4:
    if lst4.count(i)>1:
        duplicate.append(i)
for i in duplicate:
    duplicate.remove(duplicate[i%2!=0])
print(duplicate)
        

#5. take vowels and non vowels in the list,find out total num of vowels in the list

    
'''def vowels(value):
    count = 0
    for i in value:
        if (i == 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U')  in lst5:
            count+=1
    return count   
lst5=['a','e','u','d','e','k']
print("The total vowels are :",vowels(count))'''
    
lst5=['a','e','u','d','e','k','i']
vowels=['a','e','i','o','u','A','E','I','O','U']
count=0  
for lst5[i] in lst5:
    if lst5[i] in vowels:
        count+=1
print("The Count of Vowels is :",count)       


##################################################
#################################################
##############################################
#DATE ==> 27/07/2023



#Creating a SET --> dont allow duplicates
basket={'apple','orange','apple','pear','orange','banana'}
print(basket)


####
#Adding items to set
basket={'apple','orange','banana'}
basket.add('apricot')
print(basket)

# update ---> more than one value can be added but in form of LIST....
basket={'apple','orange','banana'}
basket.update(['apricot','cherry','mango'])
print(basket)

#Obtaining the Length
print(len(basket))

#Obtaining the MAX and MIN
basket2={25,34,18,6,7,59}
print(max(basket2))
print(min(basket2))

# removing from set
basket={'cherry', 'apricot', 'apple', 'banana', 'mango', 'orange'}
basket.remove('apple')
basket.discard('apricot')
print(basket)

#############
# set operrations==> union,intersection,difference
s1={'apple','orange','banana'}
s2={'gapefruit','lime','banana'}
print('Union :',s1 | s2)
print('Intersection:',s1 &s2)
print('Difference:',s1 - s2)

##########################################################
#########################################################
# Dictionary --->{Key : Value}
capitals={'Maharashtra':'Mumbai',
          'Gujrat':'Ahmedabad',
          'UP':'Lucknow',
          'Kartanaka':'Banglore',
          'Andrapradesh':'Hydrabad'}
print(capitals)

#Accesing item via keys
print('capitals[Maharashtra]:',capitals['Maharashtra'])

# adding a new entry
capitals['West Bengal']='Kolkatta'
print(capitals)

#Changing the key value
capitals['Gujrat']="Gandhinagar"
print(capitals)

#Removing an Entry
capitals.pop('UP')
print(capitals)

#deleting an entry
del capitals['West Bengal']
print(capitals)
    

#############
#iterating over keys

capitals={'Maharashtra':'Mumbai',
          'Gujrat':'Ahmedabad',
          'UP':'Lucknow',
          'Karnataka':'Banglore',
          'Andrapradesh':'Hydrabad'}
for states in capitals:
    print(states,end=', ')
    
for states in capitals:
    print(states,end=': ')
    print(capitals[states])
    
#Values keys and items
print(capitals.values())
print(capitals.keys())
print(capitals.items())

# checking key membership
capitals={'Maharashtra':'Mumbai',
          'Gujrat':'Ahmedabad',
          'UP':'Lucknow',
          'Karnataka':'Banglore',
          'Andrapradesh':'Hydrabad'}
print('Karnataka' in capitals)
print('Bihar' not in capitals)

#Dictionaries can have values in tuples
seasons={'Summer':('Feb','Mar','Apr','May'),
         'Rainy':('June','July','Aug','Sept'),
         'Winter':('Oct','Nov','Dec','Jan')}
print(seasons['Rainy'])
print(seasons['Rainy'][0])

###############
# Dictionry Methods
#==>1.cannot have duplicates
#==>2. Cannot have 2 items with same keys
dic2={"brand":"Maruti",
      "model":"Breeza",
      "year":2021,
      "year":2020}
print(dic2)

##############
#Loop Through a Dictionary,it will show only keys
for x in dic2:
    print(x)
    
#Print all values in dictionary,one by one
for x in dic2:
    print(dic2[x])
    
    
"""holypython.com
githib
stack overflow
"""


    
########################    
#



































    
    
    

