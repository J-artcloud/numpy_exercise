import numpy as np

#creating a numpy array
array = np.array([1,2,3,4])
array *= 2

#working with multisimentional array
array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                 [['J','K','L'],['M','N','O'],['P','Q','R']],
                 [['S','T','U'],['V','W','X'],['Y','Z','_']]])
print(array.ndim)  #(ndim) means num of dimension
print(array.shape)  #access the shape 
word = array[1,0,0] + array[1,1,2] + array[2,2,0] + array[0,0,2] + array[0,1,1]
print(word)

# vectorized math fxn: normal math operations
'''radii = np.array([1,2,3])
print(np.pi * radii **2 )'''
#comaparaison operator: retain aboolean array
scores = np.array([91,29,100,34,48])
print(scores[scores<50])
#array broadcasting
#filtering

array1 = np.array([[12,23,31,24,15],
                   [36,57,18,29,310]])

teenagers =  array1[array1 <18]
print(array1[(array1 >= 18) & (array1 <= 65)])

#random numbers gen
#display display my emojis
rng = np.random.default_rng()

emojis = np.array([[]])
print(rng.emojis(size(3,3 )))
print(rng.integers(low=1,high=7, size=5))





