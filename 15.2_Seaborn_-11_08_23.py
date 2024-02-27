#DATE ==> 11/08/2023

##############     Seaborn    ##############
#               =============              #



#############################################
# How to use Seaborn for Data Visualization
# pip install seaborn
import seaborn as sns
#import pandas
#import matplotlib.pyplot as plt

#Seaborn has 18 in-built datasets,
#that can be found using the following command.
sns.get_dataset_names()
df = sns.load_dataset('titanic')
df.head()

##
#Count Plot
'''
 Count-plot is used to plot the frequency of different categories
'''
sns.countplot(x='sex', data=df)
#x=name of the column
#data= the dataframe

sns.countplot
sns.countplot(x='sex',hue='survived',data=df,palette='Set1')
sns.countplot(x='sex',hue='survived',data=df,palette='Set2')

#hue --> name of categorical column to split the bars
#palette --> the color palette to be used

#################################################

# KDE plot (kernel density estimation plot)

#KDE plot
#KDE(Kernel Density Estimate) is used to plot the distribution of
# continuous data

sns.kdeplot(x='age',data=df,c='k')
#x-->name of the column

sns.displot(x='age',kde=True,bins=6,data=df)

  #kde-->It is set to False by default
  #bins-->The number of bins/bars
  
sns.displot(x='age',kde=True,bins=5,hue=df['survived'],palette='Set1',data=df)

#
df7 = df[df['age'].between(16,16)]
df7
#Distribution blo

df1 = (df[(df['age']==16) & (df['sex']=='female') &
          (df['alive']=='yes') & (df['pclass']==1 )])

df2 = (df[(df['age']==20) & (df['sex']=='male') &
          (df['alive']=='no')].reset_index(drop=True))

#


#Scatter plot 
'''
For this plot And the plots below we will be working
with the iris data set.The Iris  data set contains 
Data set Data related. 
'''
df2 = sns.load_dataset('iris')
df2.head()

#scatter plot help understand corelation between data
sns.scatterplot(x='sepal_length',y='petal_length',data=df,hue='species')


########################################

#     JOINT PLOT    #

#A joint plot is also used to plot the corelation between data

sns.jointplot(x='sepal_length',y='petal_length',data=df2,kind='reg')

sns.jointplot(x='sepal_length',y='petal_length',data=df2,kind='hist')

sns.jointplot(x='sepal_length',y='petal_length',data=df2,kind='kde')


###########################################
#Pair Plot 
sns.pairplot(df2)







