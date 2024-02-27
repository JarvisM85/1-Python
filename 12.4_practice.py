#DATE ==> 08/08/23

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


df2 =df.query("Courses == 'Spark'")
df2
df2 =df.query("Duration == '40days'")
df2
df2 =df.query("Fee == 22000")
df2

############################
import pandas as pd
import numpy as np
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fee':[20000,np.nan,26000,22000,24000],
    'Discount':[1000,5000,3000,1200,4500]
    }
df = pd.DataFrame(technologies)
df

color = ['red','black','yellow','green','blue']
df1 = df.assign(colours=color)
df1

mnccompany = ['tata','amazon','google','tesla','microsoft']
df2 = df.assign(MNC=mnccompany,Colors=color)
df2

#######################

df = pd.DataFrame(technologies)

df2 = df.assign(DIS_Per = lambda x : x.Fee * x.Discount /9000)
df2

#insert()
df2
car = ['swift','creato','lambo','bugatti','ferarri']
df2.insert(2,'CARS',car)
df2

price =[4664654,545645645,65454654,5545121,4654564564]
df2.insert(3,"COST",price)
df2
######################################

df2.shape

row = len(df2.index)
row
row = len(df2.axes[0])
row
col = len(df2.axes[1])
col

print(df2.shape[0])
print(df2.shape[1])

print(df2.iloc[:3])

print(df2[['COST','MNC']])
print(df2.iloc[ 1:3, 2: 4])

print(df2.query("Fee > 21000"))
print(df2[df2['Fee']>24000])


print(df2[df2['Fee']>24000])
print(df2.loc[df2.Fee > 24000])



print(df2.loc[df2.Fee > 25000])

#############

print(df[df['Fee'].isnull()])

print(df[df['Fee'].between(15000,24000)])

####################################

print(df[df['score'].isnull()])


print(df[df['score'].between(15,20)])

print(df[(df['attempts']<2) & (df['score']>15)])


####################################
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,34,np.nan,35],
           'attempts':[1,1,2,3,2],
           'qualify':['yes','no','yes','no','no']}
labels = ['a','b','c','d','e']
df = pd.DataFrame(exam_data,index=labels)
df
##########################
df.loc['d','score']=11.5
print(df)

df.loc['c','score']=35
print(df)

print(df['attempts'].sum())
print(df['score'].sum())

print(df['attempts'].mean())
print(df['score'].mean())
print(df.describe())
print(df['score'].max())
#################

df.loc['k'] = ['Suresh',float(25),'2','yes']
df

df.loc['z']=["Sahil",'59','5','no']
df

df.dtypes
df = df.sort_values(by=['score'],ascending=False)
df
#######################
df = df.sort_values(by=['name'],ascending=False)
df

############################
df['qualify']=df['qualify'].map({'yes':True,'no':False})
df


df['name']= df['name'].replace('Ganesh','James')
df

df['name'] = df['name'].replace('Sham','Sammy')
df

color = ['red','black','yellow','blue','orange','green']
df["Colors"]=color
df

for index,row in df.iterrows():
    print(row['name'],row['score'])


'''
✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
'''
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Python"],
    'Fee':[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30days','40days','35days','40days','60days','50days','55days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
row = ['A','B','C','D','E','F','G']
df = pd.DataFrame(technologies,index=row)
print(df.dtypes)
print(type(df))


# query()

df1 = df.query("Courses != 'Python'")
df1
df.shape
color = ['red','yellow','green','blue','white','black','orange']
car = ['bugatti','fererri','lambo','nana','BMW','RR','Audi']

df2 = df.assign(CARS=car,COLORS=color)



df3 = df2.assign(DiPe = lambda x : x.Fee * x.Discount /100)
df3



df.insert(2,'COLORS',color)

df.insert(4,'CARS',car)


df.shape


row = len(df1.columns)
print(row)


r = len(df.axes[0])
print(r)


print(df.shape[0])
print(df.shape[1])


###############################################

import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,34,np.nan,35],
           'attempts':[1,1,2,3,2],
           'qualify':['yes','no','yes','no','no']}
labels = ['a','b','c','d','e']
df = pd.DataFrame(exam_data,index=labels)
df

df1 = df.iloc[[0,1,2]]
df1

df2 = df[['name','score']]
df2

df3 = df[df['attempts']>2]
df3

df4 = df.loc[df.attempts >2]
df4

df1 = df[df['score'].isnull()]
df1


df2 = df[df['score'].between(15,20)]
df2

df3 =  df[(df['attempts']<2) & (df['score']>15)]
df3

df.loc['d','score'] = 11.5

print(df['attempts'].sum())
print(df['score'].mean())

k = ['Mario',25,4,'yes']
df.loc['k'] = k

df4 = df.sort_values(by='name',ascending=False)
df4

df5 = df.sort_values(by='score',ascending=True)
df5

df['qualify']=df['qualify'].map({'yes':True,'no':False})
df

df = df.replace('Ganesh',"James")
df

df['name']=df['name'].replace("James","Marry")
df


for index,row in df.iterrows():
    print(row['name'],row['score'])