import numpy as np

# numpy 행렬 추가
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
array3 = np.concatenate([array1,array2])

print(array3.shape)
print(array3)

# 형태 바꾸기
array4 = np.array([1,2,3,4])
array5 = array4.reshape((2,2))

print(array5)

# 행렬 형태로 만든 후 배열 세로로 합치기
array6 = np.arange(4).reshape((1,4))
array7 = np.arange(8).reshape((2,4))

# axis?? => basic_5 에서 진행
array8 = np.concatenate([array6, array7], axis=0)

print(array6)
print(array7)
print(array8)



