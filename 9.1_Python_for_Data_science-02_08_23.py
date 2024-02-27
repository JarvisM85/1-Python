#DATE ==> 02/08/2023

########   Python For Data Science   ##########
#        ==========================           #


'''
A series is used to model one dimensional data, similar to a list in 
python.The series object also have a few more bits of data, including
an #index and name.
'''


import pandas as pd
songs2 = pd.Series([145,142,38,13],name='counts')
#it is easy to ispect the index of a series (or data)

songs2.index
songs2


#The index can be string based as well
#in which case pandas indicates that the data types for the index is onject


songs3 = pd.Series([145,142,38,13],name='counts',
                   index=['Paul','John','George','Ringo'])
songs3.index
songs3

######################
'''
###  The NaN value---(null value)
#stands for ==> Not A Number,
#and  is usually ignored in arithematic operations.(similar to null in SQL)
#If you load data from CSV file an empty value for an otherwise
#numeric column will become NaN
'''
# when absolute path--> when directory is not selected
import pandas as pd
f1 = pd.read_csv('c:/1-python/age.csv')
f1


# when Relative path--> when directory is Selected
import pandas as pd
f1 = pd.read_csv('age.csv')
f1

#Absolute path(/ front slash)
import pandas as pd
f2 = pd.read_excel('c:/1-python/Bahaman.xlsx')
f2

f2 = pd.read_excel('Bahaman.xlsx')
f2


############################
# for numpy---> pip install numpy
import numpy as np
numpy_ser = np.array([145,142,38,13])
songs3[1]
numpy_ser[1]

songs3.mean()
numpy_ser.mean()

##################################
#The PANDA SERIES DATA STRUCTURE provides support for the basic crud
# operations-create, read, update and delete

#Creation
george = pd.Series([10,7,1,22],
                   index = ['1968','1769','1970','1970'],
                   name = 'George Songs')
george

#####
'''
The previous example illustrates an interesting 
feature of pandas.->The index value are strings and they 
are not unique. this can cause some confusion, but can also be useful 
when duplicate index items are needed.
'''
#######################
# Reading
# To read or select the data from a series

george['1968']

george['1970']
#we can iterate over data in series as well
#When iterating over a series
for item in george:
    print(item)

###############################
#Updating
#Updating values in a series can be little tricky as well
#To update a value for a given index label,the standard
#index assignment operation works
george['1969'] = 68
george['1969']

###############
#Deletion
# The del statement appers to have
# problems with duplicate index

s = pd.Series([2,3,4],index=[1,2,3])
del s[1]
s

##############################################
#Convert Types
#string use    .astype(str)
#interger use  .astype(int)
#numeric use   pd.to_numeric
#dateline use  pd.to_datetime
# NOTE -> that this will fail with NaN

import pandas as pd
songs_66 = pd.Series([3,None,11,9],
                     index=['George','Ringo','John','Paul'],
                     name='Counts')
songs_66.dtypes
#dtype('float64')
pd.to_numeric(songs_66.apply(str))
#There will be error
pd.to_numeric(songs_66.astype(str),errors='coerce')
# If we pass errors='coerce',
# we can see that it supports many formats
songs_66.dtypes
#Dealing with None(Nan)
#1.The .fillna method will replace them with a given value
songs_66.fillna(-1)

#2.Nan value can be dropped from,the series 
#  using .dropna
# it is the last method if not any option then
songs_66.dropna()
songs_66
#all above techniques are used in
# data preprocessing --> feature Engineering
###################################################
import pandas as pd
#Append,combining and joining two series
songs_69 = pd.Series([7,16,21,39],index=['Ram','Sham','Ghansham','Krishna'],name='Counts')
# to concatenate two series together ,
# simply use the .append
song = songs_66.append(songs_69)

###############################################
#**************************************************
###################################################
#Plotting the Series
import matplotlib.pyplot as plt
fig = plt.figure()
songs_69.plot()
plt.legend()
#######################

fig = plt.figure()
songs_69.plot(kind='bar',color='y')
songs_66.plot(kind='bar',color='r')
plt.legend()

#####################################
import numpy as np
data = pd.Series(np.random.randn(500),name='500 random')
fig = plt.figure()
ax = fig.add_subplot(111)
data.hist()

#######################
#Instructions

























