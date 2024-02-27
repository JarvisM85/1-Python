#1.Write a python program to check if a list is empty.
   
lst = [1,2,3]
count = 0
for i in lst:
    if i :
        count+=1
if count>=1:
    print("Not empty")
else :
    print("Empty")
    



#2.Using list comprehention,construct a list from the squares
#  of each element in the list.

lst = [2,4,5,6,9]
lst2 = [num**2 for num in lst]
print(lst2)





#3. Write a python script to find wether a given key is present in a dictionary or not.

dic={'Name':'Hello','Age':21,'City':'Kopargaon','Branch':'ECE'}

def check(d,k):
    x = dic.keys()
    for i in x:
        if i == k:
            return "Key Exist"
            break
    return "Not exist"
a = check(dic,'Age')
print(a)   

##########
#4.
x = [i for i in range(100,160,10)]
print(x)

a = {num:num/100 for num in x}
print(a)



#############
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

############################
'''6. You have already created data frame, write it to csv'''

df.to_csv("Test_file.csv")

#################
#7.




#8.

x = lambda x,y :[x*y]
print(x(2,3))

def mul_values(x,y):
    return x*y
a = int(input("Enter 1nd Number : "))
b = int(input("Enter 2nd Number : "))
print(mul_values(a,b))



#9.
import numpy as np
x = np.array([0,0,0,0,0])
if any(x) :
    print(" Yes , Non Zero is Present")
else:
    print("Non Zero NOT Present")



#10.
import matplotlib.pyplot as plt

l1 = [2,6,5]
l2 = [7,3,6]
plt.plot(l1,marker="+")
plt.plot(l2,marker="*")
plt.show()








#11.

import matplotlib.pyplot as plt
import numpy as np
plt.bar(['python','java','PHP','javascript','c#','c++']
        ,[22.5,23.7,8.8,8,7.7,6.7]);
plt.title('Popularity Of Language')
plt.show()



















