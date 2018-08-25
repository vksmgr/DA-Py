import numpy as np

#dot product of two matrix

mtx1 = np.array([[ 1. , 2. , 3. ], [ 4. , 5. , 6. ]]) # 2 X 3 mtx
mtx2 = np.array([[ 6. , 23. ], [ - 1 , 7 ], [ 8 , 9 ]]) # 3 X 2 mtx

print(mtx1.dot(mtx2))

#test mtx product

my_1 = np.array([[1, 2], [3, 4]])
my_2 = np.array([[5, 6], [7, 8]])
print(" product of the matrix : {}".format(my_2 @ my_1))

from numpy.linalg import inv, qr
print("inverse of the matrix {} ".format(inv(my_1)))


# psudorandom number generaton
sample = np.random.normal(size=(4,4))
print(sample)
print(" This will return the random permutation : {}".format(np.random.permutation([1,2,3,4,5,6,7,8,9])))