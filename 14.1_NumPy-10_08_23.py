#DATE ===> 10/08/2023

###########      NUMPY          ############
#              =========                 #
'''
What is NUMPY  --> For array operations(usually used for MATH operations)
The numpy library is popular open source python library used
for scientific computing applications and it stands for Numerical Python
which is consisting of multidimentional arrays
objects and a collection of routines for processing those arrays.

'''

#######
'''
While a python list can contain different data types
within a single list ,all the elements in a Numpy array 
should be homogenous.
'''

#Array in Numpy
# Create ndarray
import numpy as np
arr = np.array([10,20,30])
print(arr)

# Create a multi-dimentional array
arr = np.array([[10,20,30],[40,50,60]])
print(arr)

print(arr[0][0])

#######
#Represent the minimum dimensions
# use ndmin param to specify how many minimun
# dimensions you wanted to create an array with
#Minimum Dimension
arr = np.array([10,20,30,40],ndmin=3)
print(arr)

# change the data type
#dtype parameter
arr = np.array([10,20,30,40],dtype=complex)
print(arr)



# Get the Dimension of an array
arr = np.array([[1,2,3,4],[7,8,6,7],[9,10,11,12]])
print(arr.ndim)
print(arr)


##################################
#Finding the size of each item in the array
arr = np.array([10,20,30])
print("Each item contain in byte :",arr.itemsize)


########################
#Get the datatype of Each Array Item 
#Get the Data type of each array item
arr=np.array([10,20,30])
print(arr.dtype)    #int32

#Get the Shape and Size of array
arr = np.array([[10,20,30,40],[60,70,80,90]])
print("Array Size :",arr.size)
print("Shape :",arr.shape)

##########
# Create a sequence of integers using arange()
# Create a sequence of integers
# from 0 to 20 with step 3
arr = np.arange(0,20,3)
print(arr)

arr = np.arange(11)
print(arr)
################################################
###############################################

# Array Indexing in Numpy
#Accesss single element using index
print(arr[2])
print(arr[-2])

#################################
#Multi-Dimentional Array Indexing
# Access Multi-Dimentional array elements
# using array indexing

arr = np.array([[10,20,30,40,50],[20,30,50,10,30]])
print(arr)

print(arr.shape)  # 2->rows , 5-> columns
# now its 2-> dimentional

print(arr[0,3]) 
#print(arr[0][3])

print(arr[1,-1])

##########################################3
#Acces array elements using Slicing
arr = np.array([1,2,3,4,5,6,7,8,9])
x = arr[1:8:2]
print(x)

x = arr[-2:3:-1]
print(x)

x = arr[-2:10]
print(x)

###########################
#Indexing in Numpy
multi_arr=np.array([[10,20,10,40],[40,50,60,90],[60,10,70,80],[30,90,40,30]])
multi_arr

#Slicing array
#for multi-dimen Numpy arrays,
#you can access the elements as below

multi_arr [1,2]  # To access the value at row 1 and column 2
multi_arr [1,:]  # To get the value at row 1 and all column 
multi_arr [:,2]  # To access the value at all row  and column 1


x = multi_arr[:3,::2]
print(x)

#####################
#Integer Array Indexing
#Integer array indexing allows the selection of 
#  arbitrary items :

arr = np.arange(35).reshape(5,7)
print(arr)



#Boolean array indexing
'''
This advanced indexing occurs when an object is an array object of 
Boolean types such as may be returned from comparison operators .
Use this method when we want to pick elements from the array which 
satisfy some conditions
'''
arr = np.arange(12).reshape(3,4)  # by normal
print(arr)

rows = np.array([False,True,True])  # not 0th row only 1st and 2nd
wanted_rows = arr[rows, : ]     # in selected rows all rows And all columns
print(wanted_rows)


#########################################
#Create Numpy Array to Python List
# for 1 dimentional array

#Create array
array = np.array([10,20,30,40])
print("Array :",array)
print(type(array))

#Convert to list
lst = array.tolist()
print("lst :",lst)
print(type(lst))



# for Multi-dimentional array


array = np.array([[10,20,30,40],[50,60,70,80],[60,40,20,10]])
print(array)
lst = array.tolist()
print(lst)
print(type(lst))


#################
#Convert python List to ARRAY
 # Two methods
#1.  numpy.array()
#2.  numpy.asarray()

list = [20,40,60,80]
array = np.array(list)
print(array)
print(type(array))


list = [20,40,60,80]
array = np.asarray(list)
print(array)
print(type(array))

#########################

# Numpy Properties :
    



# Shape
array = np.array([[1,2,3],[4,5,6]])
print(array.shape)

#Resize the array

array = np.array([[10,20,30],[40,50,60]])
array
array.shape=(3,2)
print(array)


###############################
#Opertions Using in Numpy

#Numpy's operations are divided into 3 main categories :
'''
    1.Fourier Transform and Shape Manipulation
    2.Mathematical and Logical Operations
    3.Liner Algebra and Random Number Generation 

'''


# Arithematic Operations :






