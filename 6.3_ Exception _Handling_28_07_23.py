# DATE ==> 28/07/23

# Exception Handling
#--> Exceptions: issues that appear at run time or compile time
#--> Error : Occue due to absence of sysyem resources

#Exception are handled with try-except blocks 
#Exception:affects the reliability of the program

print(5/0)


#using try-except Blocks
a=5
b=6
c=a=b
print(5/0)
'''
try:
    print(5/0)
except ZeroDivisionError:
        print("You cant divide by zero !") 
'''
print(c)

##############
# using try and except 
a=5
b=6
c=a=b
#print(5/0)
try:
    print(5/0)
except ZeroDivisionError:
        print("You cant divide by zero !") 
print(c)

##################################################
# Handling the FileNotFoundError Exception
filename = 'alice.txt'
with open(filename, encoding='utf-8') as f:
    contents = f.read()
########## utf-8 imp  ############
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
    
##############################################
# Storing Data
# Storing in json file(javascript object notation)
# JSON file--> is in the form of Dictionary in {}
# What is JSON is -->stands for javascript object notation
# JSON format was developed by JAVA 
'''
example : you might allow users
---------What is JSON ? -------------
Whenever any input is taken from user
to run any Python program 
then mechanism provided is ==> JSON
data is stored and Transferred through JSON only

'''
# using json.dump() and json.load()
import json

numbers = [2,3,5,7,11,13]
filename = 'numbers.json'
with open (filename,'w') as f:
    json.dump(numbers, f)

#####

import json
username = input("What is your name ? ")
filename = 'username.json'
with open (filename,'w') as f:
    json.dump(username, f)
print(f"We'll remember you when you come back, {username}!")

##########
##Now lets write new program that greets a user whose name has already been stored
import json
filename = 'username.json'
with open (filename) as f:
    username = json.load(f)
print(f"Welcome back,{username}!")

#######
#Load the username,if it has been previously
# otherwise, prompt for the username and store it.
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name ? ")
    with open (filename,'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")

    






