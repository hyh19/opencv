import numpy as np

arr = np.array([[4, 9, 1],
                [5, 13, 6],
                [10, 8, 9]])

sorted_indexes = np.argsort(arr[:, 1])
print(sorted_indexes)
print(arr[sorted_indexes, :])
