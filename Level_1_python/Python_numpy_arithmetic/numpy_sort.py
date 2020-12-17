import numpy as np

# numpy 정렬
array1 = np.array([4,5,32,6,7])
array1.sort()

print(array1) # 오름차순
print(array1[::-1]) # 내림차순
print('========')

# 각 열을 기준으로 정렬
array2 = np.array([[1,7,6,9,5],[6,3,5,2,10]])

print(array2)
print('--------')
array2.sort(axis=0)
print(array2)


