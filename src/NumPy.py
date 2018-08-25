# Learning NumPy Library

import numpy as np

#creating ndarray

data = [[1, 2, 3 ],[4, 5, 6]]
arra = np.array(data)

print(arra)

arr0 = np.zeros(10)
print(arr0)

arr0_1 = np.zeros((2,3))
print(arr0_1)
arr_empty = np.empty((10,10))
print(arr_empty)

arr_arnage = np.arange(15)
print(arr_arnage)

arr_identity = np.identity(3)
print(arr_identity)

arr_d1 = np.array([1,2,3,4,], dtype=np.float16)
print(arr_d1)

# Arithmetic operations with arrays

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([5,6,7,8,9])

print("############Arithmetic operations of arrays###############3")
print("array orignal values {0} {1}".format(arr1, arr2))
print("addition of two arraays : {0}".format(arr1 + arr2))
print("multiplication of two arraays : {0}".format(arr1 * arr2))
print("division of two arraays : {0}".format(arr1 / arr2))
print("power  of two arraays : {0}".format(arr1 ** arr2))
print("modulus  of two arraays : {0}".format(arr1 % arr2))
print("Arithmetic scalar operations {0}".format(arr1 / 2))
print("Comparions of two arrays {0}".format(arr1 > arr2))

# Array slicing.
ar_sl = np.array(range(10))

print("array one element {}".format(ar_sl[1]))
print("array one element {}".format(ar_sl[0:2]))
print("array one element {}".format(ar_sl[-2:-1]))
ar_sl[1:3] = 12
print("array one element {}".format(ar_sl))

# slice is not copy of data it's just view of orignal array

print("Orignal array : {}".format(ar_sl))
sl_arr = ar_sl[1:3]
sl_arr[0] = 00
print("Orignal array : {}".format(ar_sl))


# Multidimentional array slicing

mdim_arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mdim_arr[1][1])

#3D Arry
arr3d = np.array ([[[ 1 , 2 , 3 ],
                    [ 4 , 5 , 6 ]],
                   [[ 7 , 8 , 9 ],
                    [ 10 , 11 , 12 ]]
                   ])

print("3D array : {0}".format(arr3d[0][0][0]))

old_arr3D = arr3d[0].copy()

arr3d[0] = 23
print(arr3d)
print("\n")
print(old_arr3D)
print("\n")
arr3d[0] = old_arr3D
print("values: {}".format(arr3d))
print("other method {}".format(arr3d[0,0,0]))

#slicing with comma
print(arr3d[1:, 1:, 2:])

#by mixing index and slice you always get slice.

print(arr3d[1, 1:, 1:])
print(arr3d[:,1:, 1:])

#Boolean indexing
names = np . array ([ 'Bob' , 'Joe' , 'Will' , 'Bob' , 'Will' , 'Joe' , 'Joe' ])
data = np.random.rand(7,4)
print(data[names == 'Bob'])
print(data[names == 'Bob', :2])
print(data[~(names == 'Bob')])

# Fancy indexing : indexing with an array
print("*************Fancy Indexing ************")
ar = np.empty((8,4))

for i in range(8):
    ar[i] = i

print(ar[[4,1,0,3]])
print(ar[[-4,-7,-8,-5]])

# passing multidimensional array
ard = np.arange(32).reshape(8,4)
print(ard)
print("000====")
print(ard[[1,2,3],[0,0,0]])

##Transpose of array : and swapping axes

arrTx = np.arange(16).reshape(2,2,4)

print(" Orignal Array :\n {}".format(arrTx))

print(arrTx.transpose((1,0, 2)))

print("000====")
#ufunc : universal function this function will take array and perform operation on it element wise
test_arr_1 = np.arange(10)
test_arr_2 = np.arange(10,20)

print(np.maximum(test_arr_1,test_arr_2))