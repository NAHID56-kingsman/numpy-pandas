''': Create a random 5x5 matrix and compute its
transpose and matrix product with itself (A^T A).'''



import numpy as np

np.random.seed(0)

arr=np.random.randint(0,10,(5,5))

print(arr)
print("----------------haha noob----------------")
print(arr.T)
print("----------------haha noob----------------")
print(arr.T @ arr)

# A.T @ A → multiplies transpose of A with A using matrix multiplication rule (this is the Gram matrix, symmetric, important in linear algebra & ML).

# A.T * A → just multiplies element-by-element (Hadamard product), which is not the same.