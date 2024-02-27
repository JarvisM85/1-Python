# DATE ==> 04/08/2023

#DataFrame 2

#DROPING  of Rows ==>

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


#Drop DataFrame Rows and Columns
df = pd.DataFrame(technologies,index=row_labels)
df
#Drop  rows by labels
df1 = df.drop(['r1','r2'])
df1

#Drop/Delete rows by index/position
df1 = df.drop(df.index[1])
df1
df1 = df.drop(df.index[[1,3]])
df1

#Delete Rows by Index Range

df1 = df.drop(df.index[2:])
df1

#When you have default indexes for rows
df = pd.DataFrame(technologies)
df1 = df.drop(0)
df1

df = pd.DataFrame(technologies)
df1 = df.drop([0,3])        #it will delete row 0 and row 3
df1 = df.drop(range[0,2])   # it will delete row 0 and row 1

##########################################################################

# Droping of Columns ==>
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java","SQL"],
    'Fee':[20000,25000,26000,22000,np.nan,21000,22000,25000],
    'Duration':['30days','40days','35days','50days','60days','','55days','35days']}
df = pd.DataFrame(technologies)
print(df)


#1.Drop Column by Name
   # Drop "Fee" Column
df2 = df.drop(["Fee"],axis=1)

df = pd.DataFrame(technologies)

#2.Explicitly using parameter name 'labels'
df2 = df.drop(labels=["Fee"],axis=1)
df2
    
#3.Alternatively you can also use columns 
   # instead of 'labels'
df2 = df.drop(columns=["Fee"],axis=1)


#4.Drop Columns by Index
print(df.drop(df.columns[1],axis=1))

df = pd.DataFrame(technologies)

#5. Using inplace = True
df.drop(df.columns[2],axis=1,inplace=True)
print(df)

df = pd.DataFrame(technologies)

#6.Drop Two or More Columns by label Name
df2 = df.drop(["Courses","Fee"],axis =1)
print(df2)

df = pd.DataFrame(technologies)

#7.Drop Two or More Columns by Index
df2 = df.drop(df.columns[[0,1]],axis =1)
df2

df = pd.DataFrame(technologies)

#8.Drop Columns From List of Columns
lisCol = ["Courses","Fee"]
df2 = df.drop(lisCol,axis=1)
print(df2)

#############################################
#############################################


