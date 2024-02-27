# DATE ==> 02/08/2023

'''
To check version of pandas ==>
'''
import pandas as pd
pd.__version__

###############################
#Create using Constructor
# Create pandas DataFrame from list
import pandas as pd
technologies = [["Spark",20000,"30days"],
                ["pandas",20000,"40days"]]
df = pd.DataFrame(technologies)
print(df)

# Since
# indexes,
#incremental 
#to both

# Add Column and row labels
column_names = ["Courses",'Fee','Duration']
row_labels = ["a","b"]
df = pd.DataFrame(technologies,columns=column_names,index=row_labels)
print(df)
#
##########################
# to check ---> Data types
df.dtypes

###################
#You can also assign custom
#data types to columns
# set custom types to DataFrame

import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
    'Fee':[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30days','40days','35days','40days','60days','50days','55days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
df = pd.DataFrame(technologies)
print(df.dtypes)

# Convert all types to best possible types
# object --> string
df2 = df.convert_dtypes()
print(df2.dtypes)

# Change All Columns to Same type
# String--> Object
# objects will remained as objects
df = df.astype(str)
print(df.dtypes)

# Change Type for one or Multiple Columns
df = df.astype({"Fee":int,"Discount":float})
print(df.dtypes)

#Convert Data Type for All Columns in a List
df = pd.DataFrame(technologies)
df.dtypes
cols = ['Fee','Discount']
df[cols] = df[cols].astype('float')
df.dtypes

# Ignores Error
df = df.astype({"Courses":int},errors='ignore')
df.dtypes

#Generates Errors
df = df.astype({"Courses":int},errors='raise')
df.dtypes

#Convert feed column to numeric type
df = df.astype(str)
df.dtypes