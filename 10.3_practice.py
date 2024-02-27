#Date ==> 06/08/2023

import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
    'Fee':[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30days','40days','35days','40days','60days','50days','55days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
df = pd.DataFrame(technologies)
print(df.dtypes)


##########
# convert dataframe --> csv 
df.to_csv('data_file.csv')

df = pd.read_csv('data_file.csv')
df
#######################

import pandas as pd
import numpy as np # --> but not needed here 
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java","SQL"],
    'Fee':[20000,25000,26000,22000,np.nan,21000,22000,25000],
    'Duration':['30days','40days','35days','50days','60days','','55days','35days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
    }
row_labels = ['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies,index=row_labels)
print(df)

df.shape
df.size
df.columns
df.columns.values
df.describe()
df.info
df.index
df.dtypes


#######################
df['Fee']
df[['Fee','Discount','Duration']]

# [startrow : endrow , startcolm : endcolm]

df['Duration'][4]

df['Fee'] =df['Fee'] - 1000
df['Fee']

df.describe()
######################################################
df.columns = ['A','B','C','D']

df2 = df.rename({'A':'s1','B':'s2'},axis=1)
df2 = df.rename({'C':'s3','D':'s4'},axis='columns')
df2 = df.rename(columns={'A':'z1','B':'z2'})


########################################################
#######################################################

import pandas as pd
ds = pd.Series([2,4,6,8,10])
ab = ds.to_list()
ab
print(type(ab))
  

import pandas as pd
ds1 = pd.Series([2,4,6,8,10,12])
ds2 = pd.Series([1,3,5,7,9])

ds=ds1+ds2
ds
ds=ds1-ds2
ds
ds=ds1*ds2
ds
ds=ds1/ds2
ds
import pandas as pd
abc = [10,20,30,40,50]
bac = pd.Series(abc)
bac
print(type(abc))



import pandas as pd
import numpy as np
xyz = np.array([11,12,13,14])
print(type(xyz))
abc = pd.Series(xyz)
abc
print(type(abc))




import pandas as pd
s1 = pd.Series(['100','200','python','300.12','400'])
s1
s2 = pd.to_numeric(s1,errors='coerce')
s2


import pandas as pd
d = {'col1':[1,2,3,4,7,11],
     'col2':[4,5,6,9,5,0],
     'col3':[7,5,8,12,1,11]}
df = pd.DataFrame(d)
df
s2=df.iloc[:,0:0+1]
s2

import pandas as pd
s = pd.Series(['100','200','python','300.12','400'])
s
abc = pd.Series(s).sort_values()
abc
xyz = pd.Series(abc).sort_index()
xyz



import pandas as pd
s = pd.Series([1,2,3,4,5],index=['A','B','C','D','E'])
print("Original Data Series :")
print(s)
s= s.reindex(index=['B','C','D','A','E'])
s



import pandas as pd
s = pd.Series([['Red','Green','White'],
               ['Red','Black'],['Yellow']])
print("Original Series of List :")
print(s)
s1 = s.apply(pd.Series)
s2 = s1.stack()
s3 = s2.reset_index(drop=True)
s3

'''
😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️😶‍🌫️ ==>
'''

import pandas as pd
import numpy as np # --> but not needed here 
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java","SQL"],
    'Fee':[20000,25000,26000,22000,np.nan,21000,22000,25000],
    'Duration':['30days','40days','35days','50days','60days','','55days','35days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
    }
row_labels = ['r0','r1','r2','r3','r4','r5','r6','r7']
df = pd.DataFrame(technologies,index=row_labels)
print(df)


df.shape
df.size
df.info 
df.describe()
df.dtypes
df.index
print(df.index)
df.columns
df.columns.values


df[['Fee','Duration']]

df['Fee'][3]

df['Fee'] = df['Fee']-500
df['Fee']

###############
#Rename
df
df.columns=['A','B','C','D']
df


#1
df1 = df.rename({'A':'x1','B':'x2'},axis=1)
#2
df2 = df.rename({'C':'z1','D':'z2'},axis='columns')


df3 = df.rename(columns={"A":'c1','B':'c2','D':'c4'})

#####################################
# Series Assignment
import pandas as pd
a = pd.Series([1,2,3,4,5])
print(type(a))
lst = list(a)
print(lst)
print(type(lst))

print(a.to_list())

import pandas as pd
ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,9])
print(ds1 + ds2)
print(ds1 - ds2)
print(ds1 * ds2)
print(ds1 / ds2)


import pandas as pd
ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,10])
print("Equal :\n",ds1==ds2)
print("Greater :\n",ds1>ds2)
print("Less:\n",ds1<ds2)

###

import pandas as pd
s1 = pd.Series(['100','200','python','300.12','400'])
s1
s2 = pd.to_numeric(s1,errors='coerce')
print(s2)

import pandas as pd
d = {'col1':[1,2,3,4,7,11],
     'col2':[4,5,6,9,5,0],
     'col3':[7,5,8,12,1,11]}
df = pd.DataFrame(data=d)

s2 = df.iloc[ : ,0]

import pandas as pd
s = pd.Series([['Red','Green','White'],
               ['Red','Black'],['Yellow']])

s1 = s.apply(pd.Series).stack().reset_index(drop=True)
#============
import pandas as pd
s = pd.Series(['100','200','python','300.12','400'])

s = pd.concat([s,pd.Series(["5000",'JAVA'])],ignore_index=True)


import pandas as pd
s = pd.Series(['100','200','python','300.12','400'])
s = s.sort_values()


import pandas as pd
s = pd.Series([1,2,3,4,5],index=['A','B','C','D','E'])
print("Original Data Series :")
print(s)
s1 = s.reindex(index=['E','B','A','C','D'])
