#Definition of an array
import numpy as np
grid = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16],
                 [17,18,19,20]])
print(grid)

print(grid[:,0])#first column
print(grid[0,:])#first row
print(grid[1,:])
print(grid[:,1])
print(grid[1][2])
print("first element",grid[0][0])

array_zero = np.zeros
print(array_zero)