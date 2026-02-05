import numpy as np

M = np.array([1, 2, 3], [4, 5, 6], [7, 8, 9])

# 1 2 3
# 4 5 6
# 7 8 9

# implement inverting a matrix using RREF
def invert(M):
    I = np.eye(M.size(0), M.size(1))

    for c in range(M.size(1)):
        