import numpy as np

# C = np.array([[1, 7],
#              [-5, 3]])
# D = np.array([[6,1],
#               [-2,3]])
# E = np.array([[2,3],
#               [7,4]])
#print(C.T)
#print(D @ E)

# F = np.array([[1,2],
#               [2,6]])
# G = np.array([[3,6],
#               [7,1]])
# F_inv = np.linalg.inv(F)
# print(np.linalg.inv(F))
# print(F_inv @ G)

# v = np.array([6,2])
# w = np.array([3,5])
# print(np.dot(v,w))

# P = np.array([[7,2],
#               [3,5]])
# Q = np.array([[9,4],
#               [3,1]])
# print(P @ Q)

S = np.array([[5,3],
              [6,4]])
T = np.array([[1,4],
              [2,6]])
S_inv = np.linalg.inv(S)

print(S_inv)
print(S_inv @ T)
