# DATE ==> 08/08/2023

#Pandas.DataFrame.query() by Examples

import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
    'Fee':[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30days','40days','35days','40days','60days','50days','55days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
row = ['A','B','C','D','E','F','G']
df = pd.DataFrame(technologies,index=row)
print(df.dtypes)


#Query all rows with Courses equals 'Spark'
df2 = df.query("Courses == 'Spark'")
print(df2)

################################################
          # .assign() is used
import pandas as pd
import numpy as np
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fee':[20000,25000,26000,22000,24000],
    'Discount':[1000,5000,3000,1200,4500]
    }
df = pd.DataFrame(technologies)
df

#1.Pandas Add Column to DataFrame
# Add new column to the DataFrame
tutors = ['Ram','sham','Ghansham','Ganesh','Ramesh']
df2 = df.assign(TutorsAssigned=tutors)
print(df2)


#2.Pandas Add Multiple Column to DataFrame
tutors = ['Ram','sham','Ghansham','Ganesh','Ramesh']
MNCCompanies = ['TATA','HCL','Infosys','Google','Amazon']
df2 = df.assign(MNC=MNCCompanies,tutors= tutors)
print(df2)


#3.Derive New Column from Existing Column
df = pd.DataFrame(technologies)
df2 = df.assign(Discount_Percent=lambda x: x.Fee * x.Discount / 100)
df2

#######
#4.Append Column to Existing pandas DataFrame
# Add New column to existing Dataframe
df = pd.DataFrame(technologies)
df
df['MNC'] = MNCCompanies
df


#5.Add Column at a specific position
#      .insert()   is used
df = pd.DataFrame(technologies)
df
df.insert(0,'Tutors',tutors)
df


#########################################
# Quick Examples of Get the Number of Rows & Column in DataFrame
rows_count = len(df.index)
rows_count
rows_count = len(df.axes[0])
rows_count
column_count = len(df.axes[1])
column_count

####
df = pd.DataFrame(technologies)
row_count = df.shape[0]
col_count = df.shape[1]
print(row_count)
print(col_count)



