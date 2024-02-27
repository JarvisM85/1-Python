

import pandas as pd
song_2 = pd.Series([45,25,35,67],name='count')
song_2.index
song_2
####

import pandas as pd
song_3 = pd.Series([45,23,79,21],name='counts',
                   index=["Paul","John","Jani","Jerry"])
song_3.index
song_3

##########
import pandas as pd
f1 = pd.read_csv("c:/1-python/age.csv")
f1

f2 = pd.read_csv("age.csv")
f2

s1 = pd.read_excel("c:/1-python/Bahaman.xlsx")

s2 = pd.read_excel("Bahaman.xlsx")

####
import numpy as np
numpy_ser = np.array([145,142,38,13])
song_3[2]
numpy_ser[1]
song_3.mean()
numpy_ser.mean()

############### 
#Creating
import pandas as pd
sam = pd.Series([12,45,36,78],
                index=['1235','4563','7895','1235'],
                name='Sam Count')
sam

# Reading
sam['4563']
sam['1235']
for i in sam:
    print(i)

###
# Updating-->

sam['4563'] = 59
sam['4563']


###
# Deletion-->

s = pd.Series([280,32,64,44],index=[1111,2213,3125,2213])
del s[2213]
s
########################################
import pandas as pd
songs_66 = pd.Series([3,None,11,9],
                      index=['George','Ringo',"John","Paul"],
                      name='Counts')
songs_66.dtypes
songs_66

#songs_66['Ringo']=45

pd.to_numeric(songs_66.apply(str),errors='coerce')

pd.to_numeric(songs_66.astype(str),errors='coerce')

songs_66.dtypes
songs_66
songs_66.fillna(-1)

songs_66.dropna()

#
#Appending
import pandas as pd
songs_69 = pd.Series([7,16,21,39],index=
                     ['Ram','Sham','Ghansham','Krishna'],
                     name='Counts')
songs_66
songs_69

songs_66.append(songs_69)
s



# plotting


###########################################################
#Date==> 06/08/23
# series

import pandas as pd
s1 = pd.Series([11,12,13,15],name='Sahil')
s1

import pandas as pd
s2 = pd.Series([25,65,656,684],index=['A','B','C','D'],name='Names')
s2 

import pandas as pd
s2 = pd.Series(['George','Ringo',"John","Paul"],index=['A','B','C','D'],name='Names')
s2

#############################################
# to read a file
import pandas as pd
f1 = pd.read_csv("c:/1-Python/age.csv")
f1
f1 = pd.read_csv("age.csv")
f1

f2 = pd.read_excel("c:/1-Python/Bahaman.xlsx")
f2
f2 = pd.read_excel("Bahaman.xlsx")
f2

#######################################
import numpy as np
num = np.array([154,465,21,654])
num
num[1]
s1[2]
s1.mean()
num.mean()
#######################################################
# Pandas Series -> Data Structure
#CURD--> create , update , read , delete

#1. Create
import pandas as pd
george = pd.Series([456,542,798,354],
                   index=['1968','1969','1970','1970'],
                   name = 'George Songs')
george
#####3
#2.Update
george['1968']=111
george
george['1970']=999
george




#3.read
george['1968']
george['1970']

george

for i in george:
    print(i)

#4.delete
s = pd.Series([2,3,4],index=[1,2,3])
s
del s[2]
s

###################################
#convert types 
'''
string use -->  .astype(str)
int use ----->  .astype(int)
to numeric -->  pd.to_numeric
datetime ---->  pd.to_datetime

'''
import pandas as pd
s1 = pd.Series([11,12,13,14],index=['sahil','abhi','aniket','prajwal'],name="Names")
s1

s2 = pd.Series([101,102,103,104],index=["A","B","C","D"],name="Songs")
s2

################################s
s1.dtypes
s2.dtypes
import pandas as pd
songs_66 = pd.Series([3,None,11,9],
                      index=['George','Ringo',"John","Paul"],
                      name='Counts')
songs_66
songs_66.dtypes
pd.to_numeric(songs_66.apply(str),errors='coerce')
songs_66.dtypes
pd.to_numeric(songs_66.astype(str),errors='coerce')
songs_66.dtypes

songs_66.fillna(-1)


songs_66.dropna()



#Append combining, and joining two series
songs_69=pd.Series([7,16,21,39],
index=['Ram','Sham','Ghansham','Krishna'],
name='Counts')
#To concatenate the two series together simly use the append
songs=songs_66.append(songs_69)
print(songs)

##########################################
#Append
import pandas as pd

s1 = pd.Series([159,25,70,111],index=['sahil','abhi','aniket','prajwal'],name="Names")
s1

s2 = pd.Series([58,115,12,36],index=["A","B","C","D"],name="Songs")
s2

s = s1.append(s2)

######################################################
####################################################3
#Plotting of Graph :
import matplotlib.pyplot as plt
fig = plt.figure()
s1.plot()
plt.legend()


import matplotlib.pyplot as plt
sol = plt.figure()
s1.plot(kind='bar',color='y')
s2.plot(kind='bar',color='r')
plt.legend()

import matplotlib.pyplot as plt
sol = plt.figure()
s1.plot(kind='pie')
plt.legend()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
sa = pd.Series(np.random.randn(500),name="Random")
fig = plt.figure()
ab = fig.add_subplot(111)
sa.hist()


###################################################

import pandas as pd
pd.__version__

####
# DataFrame--> from list
import pandas as pd
technologies = [["Spark",20000,"30days"],
                ["pandas",20000,"40days"]]
df = pd.DataFrame(technologies)
df
print(df)

colm = ["Courses","Fee","Duration"]
row = ['a','b']
df = pd.DataFrame(technologies,columns=colm,index=row)
print(df)


# DataFrame--> from Dictionary

import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
    'Fee':[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30days','40days','35days','40days','60days','50days','55days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
df = pd.DataFrame(technologies)
print(df)
print(df.dtypes)

########################################

df2 = df.convert_dtypes()
print(df2.dtypes)

df = df.astype(str)
print(df.dtypes)

df = df.astype({'Fee':int,"Discount":float})
print(df.dtypes)

df=df.astype({'Discount':int})
print(df.dtypes)

col = ['Fee','Discount']
df[col] = df[col].astype(float)
print(df.dtypes)

df = df.astype({'Courses':int},errors='ignore')
print(df.dtypes)

df = df.astype({'Courses':int},errors='ignore')
df.dtypes

df = df.astype(str)
df.dtypes

col = ['Fee']
df[col] = df[col].astype(int)
print(df.dtypes)

'''
#################@@@@#####@@@@@@@@@@@@@@@@@@@@@@@@@@
#################@@@@#####@@@@@@@@@@@@@@@@@@@@@@@@@@
#################@@@@#####@@@@@@@@@@@@@@@@@@@@@@@@@@
'''

#Series --> 1 dimentional data
  
import pandas as pd
import numpy as np
sahil = pd.Series([23,56,None,89],name='Marks',index=[10,20,40,60])
sahil

s = pd.Series([2,3,4],index=[1,2,3],name='Marks')
s
del s[3]
del sahil['phy']
sahil

import pandas as pd

abc = s.append(sahil)
print(abc)


sahil.index['math']=='hist'
sahil

for i in sahil:
    print(i)

print(type(sahil))


sahil.dtypes
sahil.shape
sahil.size
sahil.describe()
sahil.info



f1 = pd.read_csv('c:/1-Python/age.csv')
f1
print(type(f1))

f2 = pd.read_excel('c:/1-Python/Bahaman.xlsx')
f2


import numpy as np
ab = np.array([1,2,3,4,5])
print(type(ab))

ab[2]
ab.mean()


s1 = pd.Series([10,60,30,40],index=['math','phy','bio','chem'],name="Marks")
s1
print(type(s1))
s1.dtypes
pd.to_numeric(s1.apply(str),errors='coerce')
s1.dtypes
pd.to_numeric(s1.astype(str),errors='coerce')
s1.dtypes



s1
s1.fillna(-1)
s1.dropna()




# Matplotlib

import matplotlib.pyplot as plt
fig = plt.figure()
s1.plot(kind='bar',color='r')
s.plot(kind='bar',color='y')
plt.legend()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.Series(np.random.randn(500),name="Hello")
fig = plt.figure()
ax = fig.add_subplot(111)
data.hist()


import matplotlib.pyplot as plt
fig = plt.figure()
s1.plot()
plt.legend()

import matplotlib.pyplot as plt
fig = plt.figure()
sahil.plot(kind='bar',color='r')
s1.plot(kind='bar',color='y')
plt.legend()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.Series(np.random.randn(500),name="Mario")
fig = plt.figure()
x = fig.add_subplot(111)
data.hist()


'''
🥶🥶🥶🥶🥶   DataFrame   😒😒😒😒😒==>
              ------------
'''
# conda install -c anaconda pandas 
 # conda install update pandas = 2.0.3
 
import pandas as pd
pd.__version__

import pandas as pd

df = pd.DataFrame({"course":["sql","java",'python'],
                   "fee":[3214,4652,7895],"time":['35days','65days','32days']},
                  index = ['A','B','C'])
df

dic = {'A':['abc','efg','hij'],
       'B':['xyz','ccd','sbk']}
row = ['r1','r2','r3']
df1 = pd.DataFrame(dic,index=row)
df1

df2 = pd.DataFrame([['sahil','akash','sumit','aniket'],
                   ['sammy','john','sam','mario']],columns =['name','srname','head','main'],
                   index = ['A','B'])
df2

col =['name','srname','head','main']
df1 = pd.DataFrame(dic,columns=col,index=row)
df1


a1 = pd.read_csv('crime_data.csv')




df.dtypes
print(type(df))


##########################################

import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Oracle","Java"],
    'Fee':[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30days','40days','35days','40days','60days','50days','55days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
df = pd.DataFrame(technologies)
print(df.dtypes)

df1 = df2.convert_dtypes()
df1.dtypes

df2 = df.astype(str)
df2.dtypes


df1 = df1.astype({'Fee': int,'Discount':float})
df1.dtypes


col = ['Fee','Discount']
df2[col] = df[col].astype(float)
df2.dtypes

df4 = df.astype({"Courses":int},errors='ignore')
df4.dtypes

df5 = df.astype({"Courses":int},errors='raise')
df5.dtypes



df= df.astype(int,errors='ignore')
df.dtypes

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++











































