import numpy as np

# numpy 산술연산
array = np.random.randint(1, 10, size=4).reshape(2,2)
#print(array)

# 각각의 행에 곱
result_array = array * 10
#print(result_array)

# 행렬의 합
# arrang 는 0부터 n-1 까지 숫자까지 가져 오는 것
array1 = np.arange(16).reshape(4,4) # 4x4
array2 = np.arange(4).reshape(4,1) # 1x2

array3 = array1 + array2

print(array1)
print('-----')
print(array2)
print('-----')
print(array3)

# arrange(x,y) x 이상 y미만
array4 = np.arange(3,10) 
print('======')
print(array4)

# arrange(x,y,z) x 이상 y미만 z간격 으로
array5 = np.arange(3,10,2)
print('======')
print(array5)


