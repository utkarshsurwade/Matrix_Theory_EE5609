import numpy as np
from numpy import linalg

M = np.array([[1, 0], [0, 1], [2, -2 / 3]])
b = np.array([[1], [3], [0]])
U, s, V = linalg.svd(M)  # SVD
S = np.zeros(M.shape)  # diagonalizing S
S_inv = S.T
S[:2, :2] = np.diag(s)
s_inv = 1. / s

S_inv[:2, :2] = np.diag(s_inv)   # Inverse transpose of S

x = V.T.dot(S_inv).dot(U.T).dot(b)
print(x)
