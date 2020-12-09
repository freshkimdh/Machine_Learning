import numpy as np

# 배열 나누기
# split(데이터, 인덱스, axis)
array1 = np.arange(8).reshape(2,4)
left, right = np.split(array1, [2], axis=1)

print(left.shape)
print(right.shape)
print(array1)
print(left)

