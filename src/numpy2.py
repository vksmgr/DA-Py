# Array oriented programming with arrays
import numpy as np

points = np.arange(-5, 5, 0.01) #1000 equilly spaced points

print(points)
print("===========================================")

xs, ys = np.meshgrid(points, points)

print(xs)
print("===========================================")
print(ys)
print("===========================================")

print(np.sqrt(xs ** 2 + ys ** 2))

print("===========================================")


#Expressing conditional logic as array operations
xarr = np . array ([ 1.1 , 1.2 , 1.3 , 1.4 , 1.5 ])
yarr = np . array ([ 2.1 , 2.2 , 2.3 , 2.4 , 2.5 ])
cond = np . array ([ True , False , True , True , False ])

result = np.where(cond, xarr, yarr)
print(result)

# suppose we have some random array and want to replace all
#+ve values with +2 and -ve with -2 we can use
#where function
rdarray = np.random.rand(4,4)

print("===========================================")
print(rdarray)
print("===========================================")
#print(np.where(rdarray > 0, 2, -2))

#Mathematical and statistical methods

print(rdarray.mean())
print(np.mean(rdarray))
print(np.sum(rdarray))

print("===========================================")
#Testing membership of np array
arr_1 = np.array([1,2,3,4,5,6,7,8])
print(np.in1d(arr_1, [2,3]))

print("===========================================")
#File Saving and loading an array in numpy
#for saving files we use np.save() and for loading we use np.load()
arr_2 = np.arange(10).reshape(2,5)
arr_4 = np.array([10,20,30,10])
print(arr_2)


np.savez('save_array',arr_2='a', arr_4 = 'b')
arr_3 = np.load('save_array.npy')
print("Saved array was {}".format(arr_3))


arr_5 = np.array([[10,20,30],[40, 50 ,60]])
#asarray() function will  not create the copy of the array it just create the view of that array
arr_6 = np.asarray(arr_5)
print(arr_6)
arr_5[0][2] = 100
print(arr_6)

