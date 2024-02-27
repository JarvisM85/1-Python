#DATE==> 08/08/23

import pandas as pd
import numpy as np
df = pd.read_csv("Seeds_data.csv")
df

################################################
################################################
import pandas as pd
df=pd.read_csv('Seeds_data.csv')

df.shape
df.size
df.describe()

########################

df2=df.iloc[3:8,2:6]
print(df2)

df2=df.iloc[:,2:6]
df2

df2=df.iloc[4:9,:]
df2

df2=df.iloc[2]          
df2

df2 = df.iloc[[2,3,6]]   
df2 = df.iloc[1:5]       
df2 = df.iloc[:1]        
df2 = df.iloc[:3]        
df2 = df.iloc[-1:]       
df2 = df.iloc[-3:]       
df2 = df.iloc[::2]

###############################

df2=df.loc[6]              
df2=df.loc[[2,3,7]]   
df2=df.loc[1:5]          
df2=df.loc[1:5:2]

##Select multiple columns
df2=df.loc[:,['Area','length','Width']]

#Select random columns
df2=df.loc[:,['Area','length','Width']]

#Select column betn two columns
df2=df.loc[:,'Area':'Width']

#Select column  by range
#All the columns from length to end
df2=df.loc[:,'length':]





################################################
################################################

df2 = df.query("Area == 14.88")
df2

df.shape


#12. 08 August 2023

###                     ASSIGNMENT CSV FILE                          ###
#                       ===================                            #


import pandas as pd
df=pd.read_csv('Seeds_data.csv')

df.shape
df.size
df.describe()

########################

df2=df.iloc[3:8,2:6]
print(df2)

df2=df.iloc[:,2:6]
df2

df2=df.iloc[4:9,:]
df2

df2=df.iloc[2]          
df2

df2 = df.iloc[[2,3,6]]   
df2 = df.iloc[1:5]       
df2 = df.iloc[:1]        
df2 = df.iloc[:3]        
df2 = df.iloc[-1:]       
df2 = df.iloc[-3:]       
df2 = df.iloc[::2]

###############################

df2=df.loc[6]              
df2=df.loc[[2,3,7]]   
df2=df.loc[1:5]          
df2=df.loc[1:5:2]

##Select multiple columns
df2=df.loc[:,['Area','length','Width']]

#Select random columns
df2=df.loc[:,['Area','length','Width']]

#Select column betn two columns
df2=df.loc[:,'Area':'Width']

#Select column  by range
#All the columns from length to end
df2=df.loc[:,'length':]        

##################################

df2=df.query("Area==15.26")
print(df2)

df2=df.query("Area!=15.26")
print(df2)

#####################################

#Add new column to dataframe
import random
x=random.randint(0,50)
df2=df.assign(Value=x)
print(df2)

###################################

#Derive new columns from existing columns
df2=df.assign(ratio=lambda x:x.length/x.Width)
print(df2)

#Add new column to the exiting dataframe
df['Attribute']=x
print(df)

###################################

#Quick examples of get the number of rows in dataframe
rows_count=len(df.index)
rows_count
rows_count=len(df.axes[0])
rows_count
column_count=len(df.axes[1])
column_count

###############################

row_count=df.shape[0]   #Returns number of rows
print(row_count)
col_count=df.shape[1]   #Returns number of columns
print(col_count)

#################################

df.describe()

#get the first  3 rows of given dataframe
df2=df.iloc[:3]
print(df2)

#select the 'Area ' and 'Width' column
df2=df[['Area','Width']]
print(df2)

#Select specific rows and column
df2=df.iloc[2:4,1:3]
print(df2)

#select rows where Assymetry_coeff is greater than 2
df2=df[df['Assymetry_coeff']>2]
print(df2)
'''OR'''
df2=df.loc[df.Assymetry_coeff>2]
print(df2)

#Count the  number of rows and columnns
row_count=df.shape[0]   
print(row_count)
col_count=df.shape[1]
print(col_count)

#Where value in NaN
df2=(df[df['Width'].isnull()])
print(df2)

#select rows the Area is between 15 and 16
df2=df[df['Area'].between(15,16)]   ##  16 inclusive
print(df2)

'''
select the rows where Perimeter is less than 14 and Area greater than 15
'''
df2=df[(df['Area']>13) & (df['Perimeter ']<14)]   
print(df2)


#change the Area in row 4 to 15.50
df.loc[4,'Area']=15.5    
print(df)

#calculate the sum of compactness
print(df['Compactness'].sum())

#calculate mean of perimeter
print(df['Perimeter '].mean())

#append new row 'a' to dataframe with given values for each column
df.loc['a']=[15.54,14,0.893,4.9,4.0,1.555,4.99,1,35]
print(df)

#Descending
df=df.sort_values(by=['Area'] ,ascending=[False])
print(df)
#Ascending
df=df.sort_values(by=['length'] ,ascending=[True])
print(df)


#replace qualify column content values yes and no with true and false
df.Type=df.Type.map({1:True,2:False})
print(df)


#change name 'Ganesh' to 'James' in name column
df.Area=df.Area.replace(14.29,15.99)
print(df)

#insert a new column to a existing dataframe



#iterate over rows in a dataframe
for index,row in df.iterrows():
    print(row['Area'],row['length'])



import pandas as pd
import numpy as np
data = pd.DataFrame(np.random.randn(500))
df = df.assign(Points=data)
df








