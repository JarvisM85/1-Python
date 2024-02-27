#👍
#1.Write a python program to check if a list is empty.

lst = []
if lst==[]:
    print("Empty")
else:
    print("NOT")



lst = []
count = 0
for i in lst:
    count += 1
if count==0:
    print("Empty")
else:
    print("NOT")



def type_list(a):
    if a==[] :
        return "Empty"
    else:
        return "NOT"
lst = []
print(type_list(lst))


###############################
#👍
#2.Using list comprehention,construct a list 
# from the squares of each element in the list.
lst = [2,4,6,8]
lst1 = [num**2 for num in lst]
lst1

lst = [9,25,49,81]
lst2 = [num**(1/2) for num in lst]
lst2

############################
#3. Write a python script to find wether 
#a given key is present in a dictionary or not.

dic = {1:1100,12:653,32:654,13:8456}
a = int(input("Enter key :")) 
b = ['Present' if a==key else 'Absent' for key,values in dic.items()]
if 'Present' in b:
    print("Yes, Key is Present")
else:
    print("NO, Key is Absent")



dic={'Name':'Hello','Age':21,'City':'Kopargaon','Branch':'ECE'}
def check(di,ke):
    if ke in di:
        return True
    else:
        return False
        
    
x = check(dic,"jnc")
print(x)




########################################
#👍
#4. Create a list start =100,end =160, step=10
# and then create a other dict of the form that
# key,value == key,key/100 using dict comprehention

lst = [num for num in range(100,1625,159)]
lst
dic = {key:key//100 for key in lst}
print(dic)


#########################################
#👍
'''5. Create  a dataframe which comprises course,
fees and duration and add tutor column.'''

import pandas as pd
data = {'Courses':["Spark","PySpark","Hadoop"],
    'Fee':[24000,21000,22000],
    'Duration':['35days','40days','60days'],
    }
df = pd.DataFrame(data)
df

tutor = ['abc',"pqr","xyz"]
df["TUTORS"]=tutor
print(df)

#df.insert(2,"TUTOR",tutor)
#df

#############################################
#👍
'''6. You have already created
 data frame, write it to csv'''

df.to_csv("Test_data.csv")

#######################################
#7. Write python function which returns multiple values.
#👍
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(100):
    print(num)

# yield

#######################################
#👍
#8.Write a numpy program to test if any of the 
#elements of a given array are non 0. 
import numpy as np
arr = np.array([0,0,2,0,0,0])
if any(arr):
    print("Non-Zero is PRESENT")
else:
    print("Non-Zero is ABSENT")

#######################################
#9.Write a python program to plot 2 or more lines
# and set the line markers. 
import matplotlib.pyplot as plt
a = [1,15,6,11,3]
plt.plot(a,marker='*')


#######################################
#10.Write a python program to display bar chart of
# the popularity of programming languages. 
# Sample data:
#Programming languages=Java, python, php, javascript,C#,C++ 
#Popularity=22.2,23.7,8.8,8,7.7,6.7


pl = ['Java', 'python', 'php', 'javascript','C#','C++']
pp = [22.2,23.7,8.8,8,7.7,6.7]
import matplotlib.pyplot as plt
fig = plt.figure()
plt.bar(pl,pp,color='r')
plt.title("Popularity of Programming Languages")




def is_key_present(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

my_dict = {'a': 1, 'b': 2, 'c': 3}

search_key = 'b'

if is_key_present(my_dict, search_key):
    print(f"The key '{search_key}' is present in the dictionary.")
else:
  
    print(f"The key '{search_key}' is not present in the dictionary.")