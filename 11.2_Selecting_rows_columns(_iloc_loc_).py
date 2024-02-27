#DATE ==> 04/08/2023

#name of column is given by --> loc
#index of column is given by --> iloc


#   iloc syntax [ : , : ]
# Pandas Select Rows by "Index" use of "iloc" .
#                                 *********

import pandas as pd
import numpy as np # --> but not needed here 
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","None","Spark","Python"],
    'Fee':[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30days','50days','55days','40days','60days','35days','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
    }
row_labels = ['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies)
print(df)

#  iloc --> Syntax
# df.iloc[startrow:endrow , startcolm:endcolm]

df = pd.DataFrame(technologies,index=row_labels)
#Below are quick example
df2 = df.iloc[:,0:2]
df2

#This line uses the slicing operation to get DataFrame items by index
#The first slice [:] indicates to return all rows
#The secomd slice specifies that only columns

#####
df2 = df.iloc[0:2,:]
df2

###############

#Slicing specific Rows and Columns using iloc
df3 = df.iloc[1:2,1:3]
df3

df3 = df.iloc[:,1:3]
df3

#Selecting Rows by integer Index
df2 = df.iloc[2] #Select row by index
df2

df2 = df.iloc[[2,3,6]] #Select Rows by index list
df2 = df.iloc[1:5] #Select Rows by integer index range
df2 = df.iloc[:1] #Select First row
df2 = df.iloc[:3] #Select first 3 rows
df2 = df.iloc[-1:] #Select last row
df2 = df.iloc[-3:] #Select last 3 row
df2 = df.iloc[::2] #Select alternate rows

###############################
# Select rows by index "labels" using "loc" 
#                     ******************'

df2 = df.loc['r2']
df2 = df.loc[['r2','r3','r6']]
df2 = df.loc['r1':'r5']
df2 = df.loc['r1':'r5':2]

############################

# Pandas SelectColumn by name or Index

#Using loc[] to take column slices
#loc[] syntax to slice columns
#df.loc[:,start:stop:step]

##Select multiple columns 
df2 = df.loc[:,["Courses","Fee","Duration"]]

#Select Random Columns
df2 = df.loc[:,["Courses","Fee","Discount"]]

#Select Columns between two columns
df2 = df.loc[:,"Fee":"Discount"]

#Select Columns by range
df2 = df.loc[:,"Duration":]

#Select Columns by range
# All the columns upto 'Duration'
df2 = df.loc[:,:"Duration"]







