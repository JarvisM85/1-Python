#1. D

def common(lst1,lst2):
    for i in lst1:
        for j in lst2:
            if i==j:
                return "True"
               

lst1 = [1,2,3,4,5] 
lst2 = [6,7,3,8,9]
print(common(lst1,lst2))

#2. D
lst = [1,2,3,4,5,6]
lst2 = [(num+6) for num in lst ]
lst2


#3. D
string1 = "Data Science"
string1[::-1]


#4. D
 
dict1={'Name':'Sahil','Age':21,'City':'Kopargaon','Branch':'ECE'}
for key,value in dict1.items():
    print(key,value)



#5. D
dic = {"A":1000,"B":5000,"C":1500,"D":3000}
x = {key:value for key,value in dic.items() if value>=2000}
print(x)


#6. D
a = "data.txt"
with open(a,mode='rb') as f:
    b = f.read()
    print(b)
    x = b.decode()
    print(x)



#7. D
'''py program to construct
 An infinite that returns evenly's best values
 , starting with a specified number and step. 
'''
   
import itertools
ab = [i for i in range(5)]
for a in itertools.cycle(ab):
    print(a)

start =10
step=1
my_counter = it.count(start,step)
for i in my_counter:
    print(i)

#8. D

lst1 = [1,2,3,4,5,6,7,8,9,10]
lst2 = filter( lambda x:x%2==0,lst1)
lst3 = filter( lambda y:y%2 != 0,lst1)
print([x for x in lst2])
print([y for y in lst3])

#9. D

import pandas as pd
import numpy as np
data = {"name":['Anna','Dinu','Ramu','Ganu','Emily','Mahesh','Jayesh','venkat','Ajay','Dhanesh'],
        "score":[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
        "attempts":[1,3,2,3,2,3,1,1,2,1],
        "qualify":['yes','no','yes','no','no','yes','yes','no','no','yes']}
labels=['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(data,index=labels)
df



#10.


import matplotlib.pyplot as plt
import numpy as np

lst = [2,6,3,6,2]
x = plt.plot(lst,marker=".")
plt.show()































