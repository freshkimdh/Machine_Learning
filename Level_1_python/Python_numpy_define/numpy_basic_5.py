import numpy as np

# axis 의 이해
array = np.random.randint(10, size=(5,3))
print(array)

# 5,3 행렬에서 처음 5라고 생각하면 되고, 다섯개의 원소를 더한다고 보면 된다.
print(np.sum(array, axis=0))

# 5,3 행렬에서 '3' 으로 생각하면 된다.
print(np.sum(array, axis=1))

# np.identity
b = np.identity(4)
a = np.identity(4)[1:4] # "0이상 2이하" 의 행 출력

print(b)
print(a)