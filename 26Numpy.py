# 26Numpy.py
# int8, int16, int32 uint8 : unsigned int8
# -128 ~ 127         0 ~ 255

import numpy as np

A = np.array( [ [1,2,3], [4,5,6]   ] )
print(A)
print( type(A) )   # ndarray : n-dimension
print( A.dtype )
print( A.ndim )
print( A.shape )
print( A.itemsize ) # 32b = 4B
print( id(A) )
print( A.data )

print( np.arange(3) )
# arange([start], stop, [, step], dtype=None)
# range(10)
print( np.arange(3.0) )
print( np.arange(3, 10) )
print( np.arange(3, 10, 2) )

A = np.arange(3) # 0, 1, 2
print( A.dtype )

A = np.linspace(0.0, 9.0, num=5)
print(A)

x1 = np.logspace(0.1, 1, num=10)
print(x1)

A = np.arange(15)
print(A)

A = np.arange(15).reshape((5,3))
print(A)
print(A.T)

# 산술 연산
# +, -, *, /, //, %, **
print(A ** 2)

# 관계 연산 : >, <, >=, <=, !=, ==
print( A )
print( A < 5 )
print ( A % 2 == 0 )

# 논리 연산
print( (A >5 ).any()  )
print( (A >5 ).all() )

A = np.arange(1, 10)
print(A[3])
print(A[-1])
print(A[:3])

A[:5] = 99
print(A)

A = np.array([1,1,1,2,2,3,3,3,3,1,2,3 ])
print( np.unique(A) )

A = np.arange(1, 46)
np.random.shuffle(A)
print(A)
A = np.sort(A)
print(A)


