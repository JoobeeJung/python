# 27numpy.py

import numpy as np

tmp = []
data = [1,2,3,4,5, "Hello", [11,22,33]]
for x in data:
    print(x *2)
    tmp.append(x * 2)

print("tmp = ", tmp)

myArray = np.array([1,2,3,4,5])
print(myArray *3)

# numpy  : data, datatype

a = [1, 2, 3]
b = [4, 5, 6]

na = np.array([1,2,3], float)
nb = np.array([4,5,6], float)
nc = na + nb
nd = 3*na + 2*nb
print(nc)
print(nd)
print(na.dtype)

print(na % 2 ==1)

print( np.arange(1, 5, 0.5)  )

a = np.arange(10)
print("a = ", a)

# linspace , logspace

a = np.linspace(0.0, 10.0, 5)
print(a)

a = np.arange(5)
b = np.arange(5)
z = np.sqrt(a**2 + b**2)
print(z)
# ndarray
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.vstack((a, b))
print("vstack = ", c)

d = np.hstack((a, b))
print("hstack = ", d)

a = np.arange(10)
print(a.shape)
print(a)
b = a.reshape((2, 5))
print(b)

print( a>3 )

a = np.random.uniform(10,50,10).reshape(2,5)
print("uniform = ", a)

a = np.array([0, 10, 20, 30]).reshape(4,1)
b = np.array([0, 1, 2]).reshape(1,3)
print(a + b)

a = np.random.randint(1,45, 100)
print("lotto = " , a)
a = np.arange(10)
## print( np.random.shuffle(a) )

norm = np.random.randn(5,5)
print(norm)

# binary file, text file
a = np.arange(12).reshape(3,4)
print(a)
np.save("d:/np1", a) # np1.npy
fa = np.load("d:/np1.npy")
print("fa = ", fa)

# /
# /root
# / home
#       /home/kdhong/Desktop
# / bin
# / var


a = np.arange(12).reshape(3,4)
np.savetxt("d:/mytext.txt", a)
txt = np.loadtxt("d:/mytext.txt")
print("txt = ", txt)