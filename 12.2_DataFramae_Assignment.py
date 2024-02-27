#DAte ==> 08/08/23

#Assignment

'''
1.Write pandas program to create dataframe 
from a dictionary and display
Sample Data:{'X':[34,35,67,56,43],'Y':[67,46,88,97,65], 'Z':[67,89,78,65,45]}
'''
import pandas as pd
dic = {'X':[34,35,67,56,43],'Y':[67,46,88,97,65], 'Z':[67,89,78,65,45]}
df1 = pd.DataFrame(dic)
df1

######################################################
'''
2.Write pandas program to create and display dataframe from 
a specified data
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['yes','no','yes','no','no']}
Labels = ['a','b','c','d','e']
'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,34,np.nan,35],
           'attempts':[1,1,2,3,2],
           'qualify':['yes','no','yes','no','no']}
labels = ['a','b','c','d','e']
df = pd.DataFrame(exam_data,index=labels)
df
####################################################
'''
3.Write pandas program to display summary of 
basic information about the Dataframe and its data
'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,34,np.nan,35],
           'attempts':[1,1,2,3,2],
           'qualify':['yes','no','yes','no','no']}
labels = ['a','b','c','d','e']
df = pd.DataFrame(exam_data,index=labels)
df
df.describe()
df.info

####################################################
'''
4.Write pandas program to get first 3 rows of Dataframe
'''
df = pd.DataFrame(exam_data,index=labels)
df2 = df.iloc[[0,1,2]]
df2

################################################
'''
5.Write a pandas progarm to select the 'name ' and 'score' column from the 
dataframe
'''

df=pd.DataFrame(exam_data,index=labels)
print(df[['name','score']])

################################################
'''
6.Write a pandas progarm to select the specified columns and rows
'''

df=pd.DataFrame(exam_data,index=labels)
df3 = df.iloc[1:3 , 0:2]
df3

#####################################################
'''
7.Write a pandas progarm to select rows were the number
of attempts in exam is >2 .
'''
#1.
df5 = df[df['attempts']>2]
df5

#2.
df5 = df.loc[df.attempts>2]
df5

#####################################################
'''
8.Write a pandas progarm to find no. of rows and column
in a DataFrame .
'''
df.shape

rows= len(df.index)
rows

row = len(df.axes[0])
row
col = len(df.axes[1])
col

print(df.shape[0])
print(df.shape[1])

#####################################################
'''
9.Write a pandas progarm to select the rows were the
score is missing.
'''
df7 = df[df['score'].isnull()]
df7

#####################################################
'''
10.Write a pandas progarm to select the rows 
were score is between 15 and 20.
'''
df7 = df[df['score'].between(15,20)]
df7

#####################################################
'''
11.Write a pandas progarm to select the rows were the
no. of attempts in exam is less than 2 and
score greater than 15.
'''
print(df[(df['attempts']<2) & (df['score']>15)])

#####################################################
'''
12.Write a pandas progarm to change the score 
in row 'd' to 11.5 
'''
#   loc [ row_label , column_name]
df.loc['d','score']=11.5
df

#####################################################
'''
13.Write a pandas progarm to calculate the sum of
the exam attempts by the students
'''
print(df['attempts'].sum())

#####################################################
'''
14.Write a pandas progarm to calculate the Mean
of all students score
'''
print(df['score'].mean())

df.describe()

#####################################################
'''
15.Write a pandas progarm to append a new row 'k'
to dataframe
'''
df.loc['k']=['Suresh','20.5','2','yes']
df

#####################################################
'''
16.Write a pandas progarm to sort the DataFrame 
1st by name in descending
then by score in ascending
'''
df = df.sort_values(by=['name'],ascending=[False])
df
df = df.sort_values(by=['score'],ascending=[True])
df


#####################################################
'''
17.Write a pandas progarm to replace the 'qualify'
column contains the values 'yes' and 'no' with True and False.
'''
df['qualify'] = df['qualify'].map({'yes':True,'no':False})
df

#####################################################
'''
18.Write a pandas progarm to change the name 
'Ganesh' with 'James' in name column. 
'''
df['name'] = df['name'].replace('Ganesh','James')
df

#####################################################
'''
19.Write a pandas progarm to insert a new column in 
existing dataframe. 
'''
color = ['Red','Black','Blue','Yellow','Green','Orange']
df['colors']= color
df

#####################################################
'''
20.Write a pandas progarm to iterate over
rows in a dataframe.
'''
for index,row in df.iterrows():
    print(row['name'],row['score'])
    
    
#####################################################

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    