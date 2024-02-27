#Practice ---> Date:25/07/2023
print("Welcome to Pizza Hut !")
size = input("Enter the size of Pizza [S/M/L] :")
bill=0

if size=='S':
    bill=15
    peep = input("Do you want add pepperoni on pizza [Y/N] :")
    if peep=='Y':
        bill+=2
        cheese = input("Do you want extra cheese [Y/N] :")
        if cheese=='Y':
            bill+=1
            print(f"Your bill of pizza is {bill} !.")
        elif cheese=='N':
            print(f"Your bill of pizza is {bill} !.")
        else:
            print("Invalid Input !")
    elif peep=='N':
        cheese = input("Do you want extra cheese [Y/N] :")
        if cheese=='Y':
            bill+=1
            print(f"Your bill of pizza is {bill} !.")
        elif cheese=='N':
            print(f"Your bill of pizza is {bill} !.")
        else:
            print("Invalid Input !")
    else:
        print("Invalid Input !")
elif size=='M':
    bill=20
    peep = input("Do you want add pepperoni on pizza [Y/N] :")
    if peep=='Y':
        bill+=3
        cheese = input("Do you want extra cheese [Y/N] :")
        if cheese=='Y':
            bill+=1
            print(f"Your bill of pizza is {bill} !.")
        elif cheese=='N':
            print(f"Your bill of pizza is {bill} !.")
        else:
            print("Invalid Input !")
    elif peep=='N':
        cheese = input("Do you want extra cheese [Y/N] :")
        if cheese=='Y':
            bill+=1
            print(f"Your bill of pizza is {bill} !.")
        elif cheese=='N':
            print(f"Your bill of pizza is {bill} !.")
        else:
            print("Invalid Input !")
    else:
        print("Invalid Input !")
elif size=='L':
    bill=25
    peep = input("Do you want add pepperoni on pizza [Y/N] :")
    if peep=='Y':
        bill+=3
        cheese = input("Do you want extra cheese [Y/N] :")
        if cheese=='Y':
            bill+=1
            print(f"Your bill of pizza is {bill} !.")
        elif cheese=='N':
            print(f"Your bill of pizza is {bill} !.")
        else:
            print("Invalid Input !")
    elif peep=='N':
        cheese = input("Do you want extra cheese [Y/N] :")
        if cheese=='Y':
            bill+=1
            print(f"Your bill of pizza is {bill} !.")
        elif cheese=='N':
            print(f"Your bill of pizza is {bill} !.")
        else:
            print("Invalid Input !")
    else:
        print("Invalid Input !")
else:
    print("Invalid Input !")
        
####################################################

def prime_num(num):
    for i in range(2,num):
        if(num%i==0):
            return "Not a Prime Number"
            break
    return "Prime Number"
x=int(input("Enter the Number : "))
prime_num(x)

##########################################################
def checkPassword(password):
    has_upper=False
    has_lower=False
    has_num=False
    
    for ch in password:
        if ch>='A' and ch<='Z':
            has_upper=True
        elif ch>='a' and ch<='z':
            has_lower=True
        elif ch>='0' and ch<='9':
            has_num=True
    if len(password)>=8 and has_upper and has_lower and has_num:
        return True
    else:
        return False
p=input("Enter password :")
if checkPassword(p):
    print("Strong Password !")
else:
    print("Weak Password !")
    
###############################################
import string
adj=['hello','sleepy','badly','tasty','good']
noun=['green','ball','yellow','dog','cat','hulk']
import random
adj=random.choice(adj)
noun=random.choice(noun)
number=random.randrange(0,100)
char=random.choice(string.punctuation)
password = adj[::-1] + noun[::-1] + char + char + str(number)
print("The password is : %s"%password)

        
    
          
    
    