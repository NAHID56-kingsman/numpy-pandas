''' Question : Create a 1D NumPy array of the first 20 squares and reshape it into a 4x5 matrix. 
    Then compute row-wise sums.
'''
import numpy as np

arr= np.arange(1,21)**2

#arr2= list(map(int,input().split()))  i take input from user 

print(arr)

print("----------------haha noob----------------")

reshape=arr.reshape(4,5)

Asum = reshape.sum(axis=0)  #axis=1 Row-wise // and axis=0 column-wise 

print(reshape)
print("----------------haha noob----------------")
print(Asum)