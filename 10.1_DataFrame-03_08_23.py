# DATE ==> 03/08/2023

import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
    'Fee':[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30days','40days','35days','40days','60days','50days','55days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
df = pd.DataFrame(technologies)
print(df.dtypes)

######################################
# convert dataframe to csv
df.to_csv('data_file.csv')

###################################
#Create DataFrame from csv file
df = pd.read_csv('data_file.csv')
df
######################
#Pandas DataFrame --> Basic Operations

import pandas as pd
import numpy as np # --> but not needed here 
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java","SQL"],
    'Fee':[20000,25000,26000,22000,np.nan,21000,22000,25000],
    'Duration':['30days','40days','35days','50days','60days','','55days','35days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
    }
row_labels = ['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies)
print(df)

#################
# DATAFRAME Properties ->
  #for properties NO need of parenthesis ()
  # for method is required -> ()
df.shape
#(8,4)
df.size
#32
df.columns
df.columns.values
df.index
df.dtypes
df.info

#############
# Accessing one column contents-> one square bracket
df['Fee']
#Accessing two column contents
# --> double square bracket for 2 or More columns
df[['Fee','Duration']]
df[['Fee','Duration','Discount']]

###
# select certain rows and assign it to another dataframe
df2 = df[6:]
df2

df2 = df[2:6]
df2


df2 = df[2:6][1:2] ### WROng --> Doubt
df2

#Accessing certain cell value from colm 'Duration'
df['Duration'][3]

#Subtracting specific value froma columns
df['Fee'] = df['Fee']-1000
df['Fee']

##############
#Pandas to Manipulate DataFrame
# Describe DataFrame
#Describe DataFrame for all numeric columns

df.describe()
# It will show 5 number summary 

#################################################
# rename() --> Rename pandas DataFrame columns
df = pd.DataFrame(technologies,index=row_labels)

#Assigning new header by setting new column names.
df.columns=['A','B','C','D']

#########################################
#Rename  --> axis = 0 ==> operation on rows
#Rename  --> axis = 1 ==> operation on columns
#Rename columns names using rename() method.
# 3 methods are given
df.columns = ['A','B','C','D']
df2 = df.rename({'A':'c1','B':'c2'},axis=1)
df2 = df.rename({'C':'c3','D':'c4'},axis='columns')
df2 = df.rename(columns={'A':'c1','B':'c2'})

#####################################################






