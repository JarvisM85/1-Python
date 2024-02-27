#DATE==> 09/08/23

#Assignment ==> Practice of all concepts of today

###                     ASSIGNMENT IRIS.CSV                        #####
#                       ===================                            #

######################################################
#Write DataFrame to CSV file with default parameters
import pandas as pd
df = pd.read_csv('c:/2-Datasets/Iris.csv')
df
##########################################


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
df2=df.loc[:,['Id','SepalWidthCm','PetalLengthCm']]


#Select column betn two columns
df2=df.loc[:,'Id':'PetalLengthCm']


#Select column  by range
#All the columns from length to end
df2=df.loc[:,'PetalLengthCm':]        

##################################

df2=df.query("PetalLengthCm==1.4")
print(df2)


df2=df.query("PetalLengthCm!=1.4")
print(df2)


#####################################

#Add new column to dataframe
import numpy as np
data=pd.Series(np.random.randint(range(1,151)))
df2=df.assign(Points=data)


###################################



#Derive new columns from existing columns
df2=df.assign(ratio=lambda x:x.PetalLengthCm/x.SepalWidthCm)
print(df2)


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


#select the SepalLengthCm and PetalLengthCm column
df2=df[['SepalWidthCm','PetalLengthCm']]
print(df2)


#Select specific rows and column
df2=df.iloc[2:4,1:3]
print(df2)


#select rows where SepalLengthCm is greater than 5
df2=df[df['SepalLengthCm']>5]
print(df2)
'''OR'''
df2=df.loc[df.SepalLengthCm>5]
print(df2)


#Count the  number of rows and columnns
row_count=df.shape[0]   
print(row_count)
col_count=df.shape[1]
print(col_count)


#Where value in NaN
df2=(df[df['SepalLengthCm'].isnull()])
print(df2)


#select rows between 4 and 5
df2=df[df['SepalLengthCm'].between(4,5)]   ##  5 inclusive
print(df2)


'''
select the rows where PetalLengthCm is less than 2 and SepalLengthCm 
greater than 5
'''
df2=df[(df['SepalLengthCm']>5) & (df['PetalLengthCm']<2)]   
print(df2)



#change in row 4 to 1.5
df.loc[4,'PetalLengthCm']=1.5    
print(df)


#calculate the sum of PetalLengthCm
print(df['PetalLengthCm'].sum())


#calculate mean of PetalLengthCm
print(df['PetalLengthCm'].mean())


#Descending
df2=df.sort_values(by=['PetalLengthCm'] ,ascending=[False])
print(df)
#Ascending
df2=df.sort_values(by=['SepalLengthCm'] ,ascending=[True])
print(df)



#replace Species column content values Iris-setosa with true
df.Species=df.Species.map({'Iris-setosa':True})
print(df)



#change value in a specific column
df.SepalLengthCm=df.SepalLengthCm.replace(5.1,7.1)
print(df)



#iterate over rows in a dataframe
for index,row in df.iterrows():
    print(row['SepalLengthCm'],row['PetalLengthCm'])



#################################################
##############################################
# DATE ==> 09/08/23

import pandas as pd
df = pd.read_csv('c:/2-Datasets/Iris.csv')
df


def add_1000(x):
    return x+1000
df3 = ((df.Id).apply(add_1000))
df3



def add_4(x):
    return x+4
df["PetalWidthCm"] = df["PetalWidthCm"].apply(add_4)



#Apply to multiple columns
def add_10(x):
    return x+10
df[['SepalLengthCm','SepalWidthCm']] = df[['SepalLengthCm','SepalWidthCm']].apply(add_10)


###################

#using lambda
#apply lambda function to specific column
df[['SepalLengthCm','SepalWidthCm']] =df[['SepalLengthCm','SepalWidthCm']].apply(lambda x:x+50)

################
#TRANSFORM
df3=df.drop('Species',axis=1)
def add_2(x):
    return x+2
df2=df3.transform(add_2)
print(df2)


# map()
df3 = df['PetalLengthCm'] = df["PetalLengthCm"].map(lambda z :z/3)
df3

####################

#Using DataFrame.apply() & [] operator
import numpy as np
df['PetalWidthCm'] = df['PetalWidthCm'].apply(np.square)
df



#Using DataFrame.apply() & [] operator
import numpy as np
df['PetalLengthCm'] = np.square(df['PetalLengthCm'])
df


############################################
#Pandas groupby() with Examples
#      ===============   #


# for 1 column
df2 = df.groupby(['PetalWidthCm']).sum()
# for multiple
df3 = df.groupby(['SepalLengthCm','SepalWidthCm']).sum()

df3 = df.groupby(['SepalLengthCm','SepalWidthCm']).sum().reset_index()

######


col_head = list(df.columns.values)
print(col_head)

#####################################################

#Pandas Shuffle DataFrame Rows

df4 = df.sample(frac=1)
df4
df5 = df.sample(frac=0.5)
df5

df4 = df.sample(frac=1).reset_index(drop=True)
df4

df5 = df.sample(frac=0.5).reset_index(drop=True)
df5

###########################################



