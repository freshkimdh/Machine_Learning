import numpy as np

# 행렬의 내적(행렬의 곱)

A = np.array([[1,2],[4,5]])
B = np.array([[2,2],[3,3]])

print(np.dot(A,B))


# 행렬의 형상 주의 3x2 2x3 = 3x3

C = np.array([[1,2],[3,4],[5,6]])
D = np.array([[2,2,2],[3,3,3]])

print(C.shape)
print(D.shape)

print(np.dot(C,D))

