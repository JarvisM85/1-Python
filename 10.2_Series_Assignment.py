# DATE ==> 03/08/2023 

# SERIES Assignment => 


'''
1. Write python code to create and display a 
one-dimentional array-like containing an array of datasets
i.e. SERIES
'''
import pandas as pd
ds = pd.Series([2,4,6,8,10])
print(ds)

###################################################
'''
2. Write python Program to convert a Panda module Series
to python list and it,s Type
#imp
'''
#  .tolist()    ---> converts to python list
import pandas as pd
ds = pd.Series([2,4,6,8,10])
print("Pandas  Series and type")
print(ds)
print(type(ds))
print("Convert Pandas Series to python list :")
print(ds.tolist())
print(type(ds.tolist()))

###################################################
'''
3. Write python Program add,subtract,multiple and divide
Sample Series =[2,4,6,8,10],[1,3,5,7,9]
'''
import pandas as pd
ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,9])
ds = ds1 + ds2
print("Add two series :")

print(ds)
print("Subract two series :")
ds = ds1 - ds2
print(ds)
print("Multiply two series :")
ds = ds1 * ds2
print(ds)
print("Divide two series :")
ds = ds1 / ds2
print(ds)

###################################################
'''
4. Write python Program to compare the 
elements of the Series.
'''
import pandas as pd
ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,10])
print("Series1:")
print(ds1)
print("Series2:")
print(ds2)
print("Compare the elements of the Series :")
print("Equals:")
print(ds1==ds2)
print("Greater than :")
print(ds1>ds2)
print("Less than :")
print(ds1<ds2)

###################################################
## 3 ways -- list,dict,array--> to convert into series

'''
5. Write python Program to convert a dictionary
to a Pandas Series
'''
import pandas as pd
d1 = {'a':100,'b':200,'c':300,'d':400,'e':500}
print("Original Dictionary :")
print(d1)
new_series = pd.Series(d1)
print("Converted Series :")
print(new_series)

###################################################
'''
6. Write python Program to convert Numpy array
to a Pandas series.
'''
import pandas as pd
import numpy as np
n_a = np.array([10,20,30,40,50])
print("Numpy array :")
print(n_a)
new_series = pd.Series(n_a)
print("Convertes Panda Series :")
print(new_series)

###################################################
'''
7. Write python Program to change the datatype 
of given a column or a Series.
'''
import pandas as pd
s1 = pd.Series(['100','200','python','300.12','400'])
print("Original Data Series :")
print(s1)
print("Change the said data type to numerical :")
s2 = pd.to_numeric(s1,errors='coerce')
print(s2)

###################################################
'''
8. Write python Program to convert the 
first column of a DataFrame as a Series .
'''
#name of column is given by --> loc
#index of column is given by --> iloc
#   iloc syntax [ : , : ]
import pandas as pd
d = {'col1':[1,2,3,4,7,11],
     'col2':[4,5,6,9,5,0],
     'col3':[7,5,8,12,1,11]}
df = pd.DataFrame(data=d)
print("Original DataFrame :")
print(df)
s1 = df.iloc[:,0]  # all rows and 0th column
print("\n1st Column as a Series :")
print(s1)

#################################################
'''
# reset index method
9. Write python Program 
arrange in a single series using Stack .
'''
import pandas as pd
s = pd.Series([['Red','Green','White'],
               ['Red','Black'],['Yellow']])
print("Original Series of List :")
print(s)
s = s.apply(pd.Series).stack().reset_index(drop=True)
#s1 = s.apply(pd.Series)
#s2 = s1.stack()
#s3 = s2.reset_index(drop=True)
print("One Series :")
print(s)


#2nd Way                                     

import pandas as pd
s = pd.Series([['Red','Green','White'],
               ['Red','Black'],['Yellow']])
print("Original Series of List :")
print(s)
s1 = s.apply(pd.Series)
s2 = s1.stack()
s3 = s2.reset_index(drop=True)

print("One Series :")
print(s3)
#  |
#==>
'''
DataFrame --> stack() function

The Stack() function is used to stack the precribed
level(s) from columns to index.
'''

#################################################
'''
10. Write python Program to add some data to an 
existing Series.
'''
import pandas as pd
s = pd.Series(['100','200','python','300.12','400'])
print("Original Data Series :")
print(s)
print("\nData Series after adding some data :")
new_s = pd.concat([s,pd.Series([500,"php"])],ignore_index=True)
print(new_s)

#################################################
'''
11. Write python Program to sort a given Series.
'''
import pandas as pd
s = pd.Series(['100','200','python','300.12','400'])
print("Original Data Series :")
print(s)
new_s = pd.Series(s).sort_values()
print(new_s)

#################################################
''' 
#    concept--->  .reindex
12. Write python Program to change the order
of index of a given series.
'''
import pandas as pd
s = pd.Series([1,2,3,4,5],index=['A','B','C','D','E'])
print("Original Data Series :")
print(s)

s = s.reindex(index=['B','A','C','D','E'])
print("Data Series after changing the order of index :")
print(s)

#################################################











