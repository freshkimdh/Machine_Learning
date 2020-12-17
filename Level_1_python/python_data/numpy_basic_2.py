import numpy as np

# 0 부터 9까지 랜덤하게 초기화 된 배열 만들기
array1 = np.random.randint(0, 10, (3,3)) 
print(array1)

# 평균이 0이고, 표준편차가 1인 표준정규를 띄는 배열
array2 = np.random.normal(0, 1, (3,3))
print(array2)