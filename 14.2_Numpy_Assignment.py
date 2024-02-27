#DATE ==> 10/08/2023

# Numpy Assignment ::->

'''
1.Write a Numpy program to get the NumPy version and
show the Numpy
'''
import numpy as np
print(np.__version__)


#####################################################
'''
2.Write a Numpy program to test whether none of the
elements of a given array is zero.
'''
#   np.all() ==> to see zero is present or not
#    if zero present then output = False
#    if zero NOT present then output = True

import numpy as np
x = np.array([1,2,3,4])
print(x)
print(np.all(x))  

x = np.array([0,1,2,3,4])
print(x)
print(np.all(x))


#####################################################
'''
3.Write a Numpy program to test if any of the element
of a given array are Non-Zero.
'''
#   np.any() ==> to see Non-zero is present or not
#    if Non-zero present then output = True
#    if Non-zero NOT present then output = False

import numpy as np
x = np.array([1,0,0,0])
print(x)
print(np.any(x))


x = np.array([0,0,0,0])
print(x)
print(np.any(x))


#####################################################
'''
4.Write a Numpy program to test a given array element-wise
for finiteness(not infinity OR not a number)
'''
#   np.isfinite() ==> to see a finite number present or not
#    if finite number present then output = True
#    if (infinite OR Nan ) present then output = False

import numpy as np
a = np.array([1,0,np.nan,np.inf])
print(a)
print(np.isfinite(a))

#####################################################
'''
5.Write a Numpy program to test element-wise for "NaN"
of a given array.
'''
#   np.isnan() ==> to see a "Nan" present or not
#    if NaN value present then output = True
#    if NaN value Not present then output = False

import numpy as np
a = np.array([1,0,np.nan,np.inf])
print(a)
print(np.isnan(a))

#####################################################
'''
6.Write a Numpy program to test element-wise comparision
(greater,greater_equal,less and less_equal) of given 2 arrays.
'''
import numpy as np
x = np.array([3,5])
y = np.array([2,5])
print(x)
print(y)
print(np.greater(x,y))
print(np.greater_equal(x,y))
print(np.less(x,y))
print(np.less_equal(x,y))

#####################################################
'''
7.Write a Numpy program to create a 3x3 identity matrix.
'''
import numpy as np
array_2D = np.identity(3)
print(array_2D)

#####################################################
'''
8.Write a Numpy program to generate a reandom number
between 0 and 1.
'''
import numpy as np
rand_num = np.random.normal(0,1,1)
print(rand_num)


import numpy as np
rand_num = np.random.randint(0,2,100)
print(rand_num)

#####################################################
'''
9.Write a Numpy program to create a 3x4 array and 
iterate over it.
'''
import numpy as np
a = np.arange(10,22).reshape(3,4)
print(a)
for x in np.nditer(a):
    print(x,end=" ")
    print()


#####################################################
'''
10.Write a Numpy program to create a vector of length 10
with values evenly distributed between 5 and 50.
'''
#  np.linspace --> called as linespace
#  ( start, end , length of vector)
import numpy as np
v = np.linspace(10,49,10)
print(v)

#####################################################
'''
11.Write a Numpy program to create a 3x3 matrix with 
values ranging from 2 to 10.
'''
import numpy as np
x = np.arange(2,11).reshape(3,3)
print(x)

#####################################################
'''
12.Write a Numpy program to reverse an array 
(the first element becomes the last)
'''
import numpy as np
x = np.arange(12,38)
print(x)
x = x[::-1]
print(x)


import numpy as np
x = np.arange(1,7)
print(x)
print(np.flip(x))


#####################################################
'''
13.Write a Numpy program to compute the multiplication
of two matrix.
'''
import numpy as np
p = [[1,0],[0,1]]
q = [[1,2],[3,4]]
print(p)
print(q)
result1 = np.dot(p,q)
print(result1)

#####################################################
'''
14.Write a Numpy program to compute the cross product 
of given 2 matrix.
'''
import numpy as np
a = [[1,0],[0,1]]
b = [[1,2],[3,4]]
result1 = np.cross(a,b)
result2 = np.cross(b,a)
print(result1)
print(result2)

#####################################################
'''
15.Write a Numpy program to compute determinant of a
given square array
'''
import numpy as np
from numpy import linalg as LA
a = np.array([[1,0],[1,2]])
print(a)
print(np.linalg.det(a))

print(LA.det(a))

#####################################################
'''
16.Write a Numpy program to compute the eigenvalues
and right eigenvectors of a given square array.
'''
import numpy as np
m = np.mat("3 -2;1 0")
print("a/n :",m)
w,v = np.linalg.eig(m)
print("Eigenvalues of said matrix  :",w)
print("Eigenvectors of said matrix :",v)

#####################################################
'''
17.Write a Numpy program to compute inverse of 
given matrix.
'''
import numpy as np
m = np.array([[1,2],[3,4]])
print(m)
result = np.linalg.inv(m)
print(result)

#####################################################




















