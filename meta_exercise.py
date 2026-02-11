#1.) Array Creation :
import numpy as np

array1 = np.array([[1,2,3],[4,5,6]])
print(array1)
rng = np.random.default_rng(seed=1)
array2 = rng.integers(low=0 , high= 100, size=(3,3))

#print(array1)
#print(array2)

#2.) Array manipulation

print(array1[: : -1] )
print(array2.T[::, ::-1])
#3.) Array operation 
array3 = np.array([[1,2,3],
                  [4,5,6]])
array4 = np.sum((array1 + array3), axis = 0)
print(array1.shape,array3.shape)
print(array4)                   

#4.) indexing and slicing
print(array3[1: :, ])
high = array3[array3 >3 ]
print(high)

print(np.mean(array3))
print(np.std(array3))
print(np.median(array3))
print(np.arange(9).reshape(3,3))
arr = np.array([1,2,3])
array_3 = np.arange(9).reshape(3,3)
print(array_3 + arr[:, np.newaxis])