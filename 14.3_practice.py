#DATE==> 22/08/2023

lst = ["SAhil",456,65.634]
print(lst)


import numpy as np
a = np.array([[12,54,65,23,32],[12,54,32,98,65]])
a
a.dtype

b= np.array([21,24,45,45],ndmin=2)
b
print(type(b))


print(a[1][3])
print(a[0][0])

c = np.array([21,24,45,65],dtype=complex,ndmin=3)
c

abc = np.array([[21,24,45,52],[1,56,4,6]])
print(abc.ndim)

c = np.array([1,2,3,4,5,6])
print(c.ndim)
print(a.itemsize)
print(c.itemsize)
print(len(c))
print(c.itemsize)

d = np.array([1,2,3,'sjs',5,6])
print(len(d))
print(d.dtype)

a.shape
a.size

#-------------------------------
import numpy as np
x = np.arange(2,18,3)
print(x)

y = np.array([25,36,4,1,25,36,5,6,356,623])
print(y[[0,2,9]])
print(y[-5:])


t = np.array([[10,20,30,40,50],[20,30,50,10,30]])
print(t)
print(t[1,4])
print(t[1][2])
print(t.shape)
 
#++++===========================   

s = np.array([[10,20,10,40],[40,50,60,90],[60,10,70,80],[30,90,40,30]])
s
s[1,2]
s[1,:]
s[:,1]

v = np.arange(16).reshape(4,4)
v
row = np.array([True,False,False,True])
col = np.array([True,False,False,True])
result = v[0,col]
result

print(type(v))
m = v.tolist()
print(type(m))



g = [12,54,32,65,98]
print(type(g))
h = np.asarray(g)
print(type(h))


f = np.array([[10,20,30],[40,50,60]])
f
f.shape=(3,2)
f

############################################
#Assignment

import numpy as np
np.__version__
