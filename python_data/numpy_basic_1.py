import numpy as np

list_data = [1,2,3]

# 1. list를 넘파이 자료형으로 변경
array = np.array(list_data)

print(array.size)
print(array.dtype)

# 2. 0부터 3까지의 배열 만들기
array1 = np.arange(4)
print(array1)

# 3. 행렬 형태로 만들기
# 실수 타입
array2 = np.zeros((4,4), dtype=float)
print(array2)

# 1의 값을 가지는 문자 타입
array3 = np.ones((4,4), dtype=str)
print(array3)