#DATE ==> 09/08/2023 

#Using DataFrame.apply() to apply function add column

import pandas as pd
import numpy as np
data = {"A":[1,2,3],
        "B"  :[4,5,6],
        "C":[7,8,9]}
df = pd.DataFrame(data)
df

def add_3(x):
    return x+3
df2 = df.apply(add_3)
df2

# to column A
df2 = df[df["A"].apply(add_3)] # -> doubt
df2
#or
df3 = ((df.A).apply(add_3))
##############################
#Using apply function single column
def add_4(x):
    return x+4
df["B"] = df["B"].apply(add_4)

#Apply to multiple columns
df[['A','B']] = df[['A','B']].apply(add_4)

############################
#apply lambda function to each (all) column
df2 = df.apply(lambda x:x+10)
df2
#apply lambda function to specific column
df[["A","B"]] =df[["A","B"]].apply(lambda x:x+50)

##########################
# Using pandas.DataFrame.transform() to Apply Function column
# Using DataFrame.transform()
def add_2(x):
    return x+2
df = df.transform(add_2)
df
############################
# Using pandas.DataFrame.map() to Single column
df3 = df['A'] = df["A"].map(lambda A :A/2)
df3

####################################################
#Using DataFrame.apply() & [] operator
df['A'] = df['A'].apply(np.square)
df

#Using Numpy function on single column
#Using DataFrame.apply() & [] operator
import numpy as np
df['A'] = np.square(df['A'])
df

############################################
#Pandas groupby() with Examples
import pandas as pd
import numpy as np # --> but not needed here 
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python","NA"],
    'Fee':[22000,25000,23000,24000,26000,25000,25000,22000,1500],
    'Duration':['30days','50days','55days','40days','60days','35days','30days','50days','40days'],
    'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
    }
df = pd.DataFrame(technologies)
df

#use groupby() to complete the sum
df2 = df.groupby(['Courses']).sum()
# for multiple
df3 = df.groupby(['Courses','Duration']).sum()

##########
#Add Index to the grouped data
#Add Row index to the group by result
df4 = df.groupby(['Courses','Duration']).sum().reset_index()

############
####################################################

import pandas as pd
import numpy as np # --> but not needed here 
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fee':[22000,25000,23000,24000,26000],
    'Duration':['30days','50days','30days',None,np.nan],
    'Discount':[1000,2300,1000,1200,2500]
    }
df = pd.DataFrame(technologies)
df

df.columns

#get the list of all column names from headers
column_headers = list(df.columns.values)
print(column_headers)

####################################################
#Pandas Shuffle DataFrame Rows
import pandas as pd
import numpy as np # --> but not needed here 
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
    'Fee':[20000,25000,26000,23000,24000,21000,22000],
    'Duration':['30days','40days','35days','40days','60days','50days','55days'],
    'Discount':[1000,2300,1500,1200,2500,2100,2000]
    }
df = pd.DataFrame(technologies)
df

#Pandas Shuffle DataFrame rows
#Shuffle the DataFrame rows and return all rows
df1 = df.sample(frac=1)
df1
df2 = df.sample(frac=0.5)
df2

df1 = df.sample(frac=1).reset_index(drop=True)
df1

###############################################
############################################

#JOINS -->
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Python","Pandas"],
    'Fee':[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days']
    }
index_labels = ['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies,index=index_labels)
df1

technologies2 = {
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
    }
index_labels2 = ['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2,index=index_labels2)
df2
####################
#Pandas inner join is mostly used join,
#It is used to join two dataframes on indexes
#When indexes dont natch the rows get dropped from bloth dataframe

#Pandas join , by default it will join the table left join
df3=df1.join(df2,lsuffix="_left", rsuffix="_right")
print(df3)

#Left join
df3 = df1.join(df2,lsuffix="_left",rsuffix="_right",how='left')
df3
#Inner join
df4=df1.join(df2,lsuffix="_left", rsuffix="_right",how='inner')
print(df4)
#Right join
df5=df1.join(df2,lsuffix="_left", rsuffix="_right",how='right')
print(df5)
####################################
#pandas join on columns
#inner join
df6 = df1.set_index('Courses').join(df2.set_index('Courses'),how='inner')
print(df6)
#left join
df7 = df1.set_index('Courses').join(df2.set_index('Courses'),how='left')
print(df7)
#right join
df8 = df1.set_index('Courses').join(df2.set_index('Courses'),how='right')
print(df8)
df9 = df1.set_index('Courses').join(df2.set_index('Courses'),how='cross')
print(df9)
df10 = df1.set_index('Courses').join(df2.set_index('Courses'),how='outer')
print(df10)

###################
# Using pandas.merge()   --> For Inner Join
df3 = pd.merge(df1,df2)

##############################################################
#Use pandas.concat() to concat two DataFrame
import pandas as pd
df = pd.DataFrame({'Courses':["Spark","PySpark","Python","Pandas"],
                  'Fee':[20000,25000,22000,30000]})
df1 = pd.DataFrame({'Courses':["Pandas","Hadoop","Hyperion","Java"],
                  'Fee':[25000,25200,24500,24900]})

#use pandas.concat() to concat two dataframe
data = [df,df1]
df2 = pd.concat(data)
df2

data = [df,df1]
df3 = pd.concat(data).reset_index(drop=True)
df3

################################################
#Concatenate Multiple DataFrame Using pandas.concat()
import pandas as pd
df = pd.DataFrame({'Courses':["Spark","PySpark","Python","Pandas"],
                  'Fee':[20000,25000,22000,24000]})
df1 = pd.DataFrame({'Courses':["Unix","Hadoop","Hyperion","Java"],
                  'Fee':[25000,25200,24500,24900]})
df2 = pd.DataFrame({'Duration':["30days","40days","35days","60days","55days",],
                  'Discount':[1000,2300,2500,2000,3000]})

#Appending multiple DataFrame
df3 = pd.concat([df,df1,df2])
print(df3)

df4 = pd.concat([df,df1,df2]).reset_index(drop=True)
print(df4)






