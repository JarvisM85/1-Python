#Date ==> 06/08/2023

#Dataframe droping rows and columns
######################################

# ROWS==:
import pandas as pd
import numpy as np # --> but not needed here 
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","None","Spark","JAVA"],
    'Fee':[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30days','50days','55days','40days','60days','35days','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
    }
row_labels = ['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies,index=row_labels)
print(df)


#1.
df1 = df.drop(['r5','r7'])
df1
#2.
df1 = df.drop(df.index[4])
df1
df1 = df.drop(df.index[[1,2,3]])
df1
#3.
df1 = df.drop(df.index[3:])
df1
#4.
# for default index 
df = pd.DataFrame(technologies)
df

df1 = df.drop(7)
df1

df = pd.DataFrame(technologies)
df
df1 = df.drop([0,3])
df1
df1 = df.drop(range(0,4))
df1

#############################

df1 = df.drop(['r1','r4','r6'])
df1

df1 = df.drop(df.index[3])
df1
df1 = df.drop(df.index[[4,5,7]])
df1
df1 = df.drop(df.index[3:])
df1

df = pd.DataFrame(technologies)
df

df1 = df.drop(7)
df1

df1 = df.drop([4,5,6,7])
df1

df1 = df.drop(range(2,6))
df1
####################################################
####################################################

# Droping of Columns ==>
import pandas as pd
import numpy as np
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java","SQL"],
    'Fee':[20000,25000,26000,22000,np.nan,21000,22000,25000],
    'Duration':['30days','40days','35days','50days','60days','','55days','35days']}
df = pd.DataFrame(technologies)
print(df)

df2 = df.drop(['Fee','Duration'],axis=1)
df2

df2 = df.drop(labels=['Courses','Duration'],axis=1)
df2
df2 = df.drop(columns=['Courses'],axis=1)
df2

df2 = df.drop(df.columns[[0,1,2]],axis='columns')
df2

df1 = df.drop(df.columns[:2],axis=1)
df1

df.drop(df.columns[[0,1]],axis=1,inplace=True)
print(df)


df = pd.DataFrame(technologies)
df
lst1 = ['Fee','Duration']
df1 = df.drop(lst1,axis=1)
df1

#################################################3
#################################################3

#  iloc
import pandas as pd
import numpy as np # --> but not needed here 
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","None","Spark","JAVA"],
    'Fee':[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30days','50days','55days','40days','60days','35days','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
    }
row_labels = ['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies,index=row_labels)
print(df)

df2 = df.iloc[ : , 0]
df2

df2 = df.iloc[  2:  , :]
df2


df2 = df.iloc[[2,4,7]]
df2
df2 = df.iloc[1:5]
df2

df2 = df.iloc[::2]
df2

df2 = df.iloc[-5:-1]
df2

###############################################

# --> loc 

df1 = df.loc[['r0','r4','r7']]
df1


'''
🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼
'''
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
df.index = [row_labels]
print(df)

df1 = df.drop(['r1','r2','r5'])

df2 = df.drop(df.index[[5,6,7]])


df3 = df.drop(df.index[2:6])

df4 = df.drop(range(0,5))


df5 = df.drop(df.index[2:])

#_--------------------------------------------------

df1 = df.drop(["Fee"],axis=1)

df2 = df.drop(columns=["Duration","Courses"],axis=1)

df3 = df.drop(df.columns[0],axis=1)

df4 = df.drop(df.columns[[0,2,3]],axis=1)

df5 = df.drop(df.columns[1:3],axis=1)


df.drop(df.columns[2],axis=1,inplace=True)
df


col = ["Courses","Discount"]
df5 = df.drop(col,axis=1)

#****************************************************
# iolc and loc

df1 = df.iloc[::2]
print(df1)

#loc
df2 = df.loc[:'r5',"Courses"]
df2





