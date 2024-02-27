# DATE :--> 25/07/2023
#FUNCTIONS ==>
""" function name only in small letters
    and no space in between
"""
def prime_num(num):
    for i in range(2,num):
        if(num%i==0):
            return "NOT Prime"
            break
    return "Is Prime"
x=int(input("Enter num :"))
print(prime_num(x))

##################################
#function without argument
def greet_user():
#"""Display a simple Greeting."""
    print("Hello!")
greet_user()
#########################################
#Passing Information to a function
def greet_user(username):
    print(f"Hello, {username} !")
greet_user("Sanjivani AI")

#########################################
#Arguments and Parameters

def describe_pet(animal_type,pet_name):  #---->positional arguments:
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")
describe_pet("Dog","Moti")
#order maters of dog and moti 

def describe_pet(animal_type="Dog",pet_name="Moti"):  #---->positional arguments:
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")
describe_pet()

def describe_pet(animal_type,pet_name="Kittu"):  #---->positional arguments:
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type="Dog")

############################################
#Avoiding Argument Errors
def describe_pet(animal_type,pet_name):  #---->positional arguments:
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet()

########################################################
# Assignment 1:
from datetime import datetime
def calculate_remaining_time(birth_date):
    current_date = datetime.now().date()
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
    target_date = birth_date.replace(year=birth_date.year + 80)
    remaining_time = target_date - current_date
    days_left = remaining_time.days
    weeks_left = days_left // 7
    months_left = days_left // 30
    return days_left, weeks_left, months_left
if __name__ == "__main__":
    birth_date_input = input("Enter your birth date in the format YYYY-MM-DD: ")
    try:
        days_left, weeks_left, months_left = calculate_remaining_time(birth_date_input)
        print("You have approximately:")
        print(f"{days_left} days left until you turn 80.")
        print(f"{weeks_left} weeks left until you turn 80.")
        print(f"{months_left} months left until you turn 80.")
    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD.")
        
############################################
def days_left(age):
    age_left=80-age
    days=365*age_left
    weeks=52*age_left
    months=12*age_left
    return f"You have {days} days, {weeks} weeks, {months} months remained"
age=int(input("Enter your age"))
print(days_left(age))
    
 ###########
print("What is todays age ---->")
years_today=input("Years:")
months_today=input('Months:')
days_today=input('Days:')
total_days_today=int(years_today)*365+int(months_today)*30+int(days_today) 
print(f"Your total age today in days {total_days_today}")
print("Let us assume you are expected to live 90 years")
total_days_to_live = 90*365
remaining_days_to_live=total_days_to_live-total_days_today
print(f"Your remaining life in days {remaining_days_to_live}")
    
 ###################################################   
# Assignment 2:
print("Welcome to Roller Coaster !")
height=int(input("Enter the height in \"cm\" :"))
if height >=120 :
    age=int(input("Enter the age   : "))
    if age < 12 and height==120:
        print("You are eligible to play Rollar Coaster & Price of ticket is 10 Rs.")
    elif 12<age<=18 and height==120 :
        print("You are eligible to play Rollar Coaster & Price of ticket is 15 Rs.")
    elif age<=18 and height>120:
        print("You are eligible to play Rollar Coaster & Price of ticket is 20 Rs.")
    elif age>18 and height>=120:
        print("You are eligible to play Rollar Coaster & Price of ticket is 50 Rs.")
    
else:
    print("You are NOT eligible to play Rollar Coaster.")
    
#################################################
print("Welcome tp roller coaster")
height=int(input("Enter a height: "))
bill=0
if height>=120:
    print("U are eligible to play rolar coastar")
    age=int(input("Enter your age:"))
    if age<12:
        print("Your bill is Rs 5 Rs")
        bill=5
    elif age<=18:
        print("Your bill is Rs 10")
        bill=10
    else:
        print("Your bill is Rs 15")
        bill=15
    want_photo=input("Do you want photo Y or N : ")
    if want_photo=='Y':
        bill+=3
        print(f"Your bill is Rs {bill}.")
    else:
        print(f"Your bill is Rs {bill}.")
     
else:
    print("NOT Eligible !")

######################################
users=["admin","employee","manager","worker","staff"]
for user in users:
    if user=="admin":
        print("Hello admin,would you like to see ststus report ?")
    elif user=="employee":
        print("hello employee")
    elif user=="manager":
        print("hello manager")
    elif user=="worker":
        print("hello worker")
    else:
        print("hello")
        
#############################################
#Assignment : Password Picker

import string
#Pick adjectives
adjectives=['sleepy','slow','smelly','wet','fat','red','orange','yellow','green']
#pick nouns
nouns=['apple','dinosaur','ball','toaster','goat','dragon','hammer','duck','panda']
#pick the words
import random
adjectives=random.choice(adjectives)
nouns=random.choice(nouns)
#Select number
number = random.randrange(0,100)
#select special character
special_char = random.choice(string.punctuation)
#create new secure password
password = adjectives + nouns + special_char + str(number)
print('Your new password is: %s' % password)


########################################
print("Welcome to Password Picker")
while True:
    adjectives=random.choice(adjectives)
    nouns=random.choice(nouns)
    #Select number
    number = random.randrange(0,100)
    #select special character
    special_char = random.choice(string.punctuation)
    #create new secure password
    password = adjectives + nouns + special_char + str(number)
    print('Your new password is: %s' % password)
    response=input('Would you like to generate another password ?\nType Y or N :')
    if response=='N':
        break
    
###############################################

#write code for the password is good or weak
#must follow following conditions
#1.atleast 8 characters
#2.atleast one upper case letter
#3.one lowercase
def checkPassword(password):
    has_upper= False
    has_lower= False
    has_num= False
#check each character in password and see which meets requirements
    for ch in password:
        if ch>="A" and ch<="Z":
            has_upper=True
        elif ch>="a" and ch<="z":
            has_lower=True
        elif ch>="0" and ch<="9":
            has_num=True
    if len(password)>=8 and has_upper and has_lower and has_num:
        return True
    else:
        return False

p=input("Enter a Password :")
if checkPassword(p):
    print("Strong Password")
else:
    print("Weak Password")
    
###########################################
#Write a program to cal pizza order
#bill 
#is small pizze 15$
#medium 20
#Large 25$
#to add paperony on small +2$
#paperony on meduim or large +3
#for extra cheeze on any zize +1$

print("Welcome to Pizza Hut")
size = input("Please enter size of pizza --> S,M,L :")
bill=0
if size=='S':
    bill=15
    pepperoni=input("Do you want pepperoni on pizza Y or N : ")
    if pepperoni=='Y':
        bill+=2
        extra_cheese=input("Do you want extra cheese Y or N :")
        if extra_cheese=='Y':
            bill+=1
            print(f"Your bill of pizza is {bill} $.")
        else:
            print(f"Your bill of pizza is {bill} $.")
    elif pepperoni=='N':
        extra_cheese=input("Do you want extra cheese Y or N :")
        if extra_cheese=='Y':
            bill+=1
            print(f"Your bill of pizza is {bill} $.")
        else:
            print(f"Your bill of pizza is {bill} $.")
            
elif size=='M':
    bill=20
    pepperoni=input("Do you want pepperoni on pizza Y or N : ")
    if pepperoni=='Y':
        bill+=3
        extra_cheese=input("Do you want extra cheese Y or N :")
        if extra_cheese=='Y':
            bill+=1
            print(f"Your bill of pizza is {bill} $.")
        else:
            print(f"Your bill of pizza is {bill} $.")
    elif pepperoni=='N':
        extra_cheese=input("Do you want extra cheese Y or N :")
        if extra_cheese=='Y':
            bill+=1
            print(f"Your bill of pizza is {bill} $.")
        else:
            print(f"Your bill of pizza is {bill} $.")
elif size=='L':
    bill=25
    pepperoni=input("Do you want pepperoni on pizza Y or N : ")
    if pepperoni=='Y':
        bill+=3
        extra_cheese=input("Do you want extra cheese Y or N :")
        if extra_cheese=='Y':
            bill+=1
            print(f"Your bill of pizza is {bill} $.")
        else:
            print(f"Your bill of pizza is {bill} $.")
    elif pepperoni=='N':
        extra_cheese=input("Do you want extra cheese Y or N :")
        if extra_cheese=='Y':
            bill+=1
            print(f"Your bill of pizza is {bill} $.")
        else:
            print(f"Your bill of pizza is {bill} $.")
else:
    print(f"Your bill of pizza is {bill} $.")
            
    
    
    
    





