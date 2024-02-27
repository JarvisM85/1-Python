
import pandas as pd
import numpy as np
dic = {'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]}
df = pd.DataFrame(dic)
df

###################################################

def add_50(x):
    return x+1000
df2 = df.apply(add_50)
df2

df3 = df[df["A"].apply(add_50)]

df3 = df["A"].apply(add_50)
df3
df3 = ((df.A).apply(add_50))
df3
#############################
def add_10(x):
    return x+10
df = df.apply(add_10)
df

df["B"] = df["B"].apply(add_10)
df

df[["A","C"]] = df[["A","C"]].apply(add_10)
df

df4 = df.apply(lambda x:x+10)
df4
df[["A","C"]] = df[["A","C"]].apply(lambda x : x+100)
df

##############################
def add_50(x):
    return x+50
df = df.transform(add_50)
df

#map()
df5 = df["A"] = df["A"].map(lambda A:A/2)

#######################################################

df2["A"] = df2["A"].apply(np.square)
df2


df2 = np.square(df2["C"])
df2

###################################################
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

df2 = df.groupby(["Courses"]).sum()
df2

df3 = df.groupby(["Courses","Duration"]).sum()
df3

df3 = df.groupby(["Courses","Duration"]).sum().reset_index()


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
col_head = list(df.columns.values)
print(col_head)

######################################################

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

df1 = df.sample(frac=1)
df1

df1 = df.sample(frac=0.25)
df1
df1 = df.sample(frac=0.5).reset_index(drop=True)
df1

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

df3 = df1.join(df2,lsuffix='_left',rsuffix='_right')
df3
df4 = df1.join(df2,lsuffix='_left',rsuffix='_right',how='left')
df4
df5 = df1.join(df2,lsuffix='_left',rsuffix='_right',how='inner')
df5

df4 = df1.join(df2,lsuffix='_left',rsuffix='_right',how='left')
df4
df6 = df2.join(df1,lsuffix='_left',rsuffix='_right',how='right')
df6


df7 = df1.join(df2,lsuffix='_left',rsuffix='_right',how='outer')
df7

##################################################33

df3 = df1.set_index("Courses").join(df2.set_index("Courses"),how='inner')
df3

df4 = df1.set_index("Courses").join(df2.set_index("Courses"),how='left')
df4
df5 = df1.set_index("Courses").join(df2.set_index("Courses"),how='right')
df5
df6 = df1.set_index("Courses").join(df2.set_index("Courses"),how='outer')
df6
df7 = df1.set_index("Courses").join(df2.set_index("Courses"),how='cross')
df7

#####################################################
df8 = pd.merge(df1,df2)

#######################################
import pandas as pd
df = pd.DataFrame({'Courses':["Spark","PySpark","Python","Pandas"],
                  'Fee':[20000,25000,22000,30000]})
df1 = pd.DataFrame({'Courses':["Pandas","Hadoop","Hyperion","Java"],
                  'Fee':[25000,25200,24500,24900]})



data = [df,df1]
df2 = pd.concat(data)
df2

df3 =df2.reset_index(drop=True)

#Concatenate Multiple DataFrame Using pandas.concat()
import pandas as pd
df = pd.DataFrame({'Courses':["Spark","PySpark","Python","Pandas"],
                  'Fee':[20000,25000,22000,24000]})
df1 = pd.DataFrame({'Courses':["Unix","Hadoop","Hyperion","Java"],
                  'Fee':[25000,25200,24500,24900]})
df2 = pd.DataFrame({'Duration':["30days","40days","35days","60days","55days",],
                  'Discount':[1000,2300,2500,2000,3000]})

dat = [df,df1,df2]
df3 = pd.concat(dat)
df3

df4 = df3.reset_index(drop=True)

'''
✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
'''
import pandas as pd
import numpy as np
data = {"A":[1,2,3],
        "B"  :[4,5,6],
        "C":[7,8,9]}
df = pd.DataFrame(data)
df


def add_10(num):
    return num+10
df1=df.apply(add_10)
df1

df2 = df['A'].apply(add_10)
df2

df3 = df['A'].apply(add_10)

df4 = ((df.A).apply(add_10))
print(df4)


df2 = df["A"].apply(add_10)
df2

df3 = (df.A).apply(add_10)
df3

def add_50(num):
    return num+50 
df[["A","C"]]=df[["A","C"]].apply(add_50)
df

df5= df.apply(lambda x:x+100)
df5

df6 = df[["A","C"]].apply(lambda x : x+500)
df6

########@@@@@@--------------------------


def add_10(num):
    return num+10
df = df.transform(add_10)
df


df
df["A"] = df["A"].apply(lambda x : x/2)
df

df["A"]=df["A"].map(lambda A:A/2)
df

df["A"]=df["A"].apply(np.square)
df





df["A"]=np.square(df["A"])
df


###################
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

df1 = df.groupby(["Courses"]).sum()
df1

df2 =df.groupby(["Courses","Fee"]).sum()
df2

df4 = df.groupby(["Courses","Duration"]).sum().reset_index()
df4

df.columns.values

###########################################
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

df1 =df.sample(frac=1).reset_index(drop=True)

############################################
#Joins
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

df3 = df1.join(df2,lsuffix='_left',rsuffix='_right')
df3

df4 = df1.join(df2,lsuffix="_left",rsuffix="_right",how='cross')
df4


#########################################
df5 = df1.set_index("Courses").join(df2.set_index("Courses"),how='inner')
df6 = df1.set_index("Courses").join(df2.set_index("Courses"),how='left')
df7 = df1.set_index("Courses").join(df2.set_index("Courses"),how='right')
df8 = df1.set_index("Courses").join(df2.set_index("Courses"),how='outer')
df9 = df1.set_index("Courses").join(df2.set_index("Courses"),how='cross')

dfa = pd.merge(df1,df2)



data = [df1,df2]
df3 = pd.concat(data)


import pandas as pd
df = pd.DataFrame({'Courses':["Spark","PySpark","Python","Pandas"],
                  'Fee':[20000,25000,22000,30000]})
df1 = pd.DataFrame({'Courses':["Pandas","Hadoop","Hyperion","Java"],
                  'Fee':[25000,25200,24500,24900]})

data = [df,df1]
df4 = pd.concat(data).reset_index(drop=True)

import pandas as pd
df = pd.DataFrame({'Courses':["Spark","PySpark","Python","Pandas"],
                  'Fee':[20000,25000,22000,24000]})
df1 = pd.DataFrame({'Courses':["Unix","Hadoop","Hyperion","Java"],
                  'Fee':[25000,25200,24500,24900]})
df2 = pd.DataFrame({'Duration':["30days","40days","35days","60days","55days",],
                  'Discount':[1000,2300,2500,2000,3000]})


df6 = pd.concat([df,df1,df2]).reset_index(drop=True)






