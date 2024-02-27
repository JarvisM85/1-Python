#DATE ==> 31/07/2023

'''
1.Find all the numbers from 1-1000 that are div by 7
'''
lst = [num for num in range(1,1000) if num%7==0]
print(lst)

##################################################
'''
2.Find all the numbers from 1-1000 that have 3 in them
'''
lst = [i for i in range(1,1000) if '3' in str(i)]
print(lst)


##################################################
'''
3.Count the number of spaces in a string
'''

some_string = 'the slow solid squid swam sumptuously through the silly swamp'
space = [s for s in some_string if s==' ']
print(len(space))

##################################################
'''
4.Create a list of all the consonants in the string
# "Yellow Yaks like yelling and yawing and yesterday they yodled while eating yuky yams"
'''
sentence = "Yellow Yaks like yelling and yawing and yesterday they yodled while eating yuky yams"
lst = [c for c in sentence if c not in 'a,e,i,o,u,' '']
print(lst)
#########################################################
'''
5. Find comman numbers in two lists (without using tuple or set)
'''
list_a = [1,2,3,4]
list_b = [2,3,4,5]
common = [a for a in list_a if a in list_b]
print(common)
#####################################################
'''
6.Get only the numbers in a sentence like 'In 1984 there were 12 instances of a protest with 1000 attending'
'''
sentence = 'In 1984 there were 12 instances of a protest with 1000 attending'
words = sentence.split()
result = [number for number in words if not number.isalpha()]
print(result)

#####################################################
'''
7.Given numbers = range(20) ,produce a list containing the word 'even' and 'odd'
'''
result = []
for n in range(20):
    if n%2==0:
        result.append("even")
    else:
        result.append("odd")
print(result)
###
#by list comprehension
result = ['even' if n%2==0 else 'odd' for n in range(20)]
print(result)

#####################################################
'''
8. Produce a list of tuple consisting of only the
matching numbers in these lines 
list_a = [1,2,3,4,5,6,7,8,9]
list_b = [2,7,1,12].result would match look like (4,4),(12,12)
'''
list_a = [1,2,3,4,5,6,7,8,9]
list_b = [2,7,1,12]
result = [(a,b) for a in list_a for b in list_b if a==b]
print(result)

#######################
'''
#same above code for some matching words
'''
#####################################################
'''
10. find all of the words in a string that are less 
than 4 letters
'''
sentence = 'On a summer day Ramnath sonar went swimming in the sun and his red skin stung'
examine = sentence.split()
result = [words for words in examine if len(words)<4]
print(result)

########################################################
'''
11. Write python program to print a specified list
after removing the 0th,4th,5th element
'''
color = ['Red','Green','White','Black','Pink','Yellow']
color = [x for (i,x) in enumerate(color) if i not in(0,4,5)]
print(color)
########################################################
'''
12. Write a py program that creates a generator function
that yields cubes of numbers from 1 to n .Accept n from user
'''
def cube_generator(n):
    for i in range(1,n+1):
        yield i**3
n = int(input("Input a number :"))
# create cube generator
cubes = cube_generator(n)
print("Cubes of numbers from 1 to", n)
for num in cubes:
    print(num)

#########################################################
'''
13. Write a py program to implement a generator
 that generates random numbers within a given range
'''
import random
def random_number_generator(start,end):
    while True :
        yield random.randint(start,end)
    
start = int(input("Enter the start value :"))
end  = int(input("Enter the end value :"))

random_numbers = random_number_generator(start, end)
print("Random numbers between",start,"and",end)
for _ in range(10):
    print(next(random_numbers))

#########################################################
'''
14. Write a python program to generate a 3*4*6 3D array 
whose each element is *.
'''
array = [[['*' for col in range(6)]for col in range(4)]for row in range(3)]
print(array)

#########################################################
'''
15. Write a Python program to print the numbers of a specified 
list after removing even numbers
'''
num = [7,8,120,25,44,20,27]
lst =[x for x in num if x%2!=0]
print(lst)






























