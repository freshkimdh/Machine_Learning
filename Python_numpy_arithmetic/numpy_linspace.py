import numpy as np

# 균일한 간격으로 데이터 생성
# 0부터 10 사이를 5개의 데이터를 채우는 것
array = np.linspace(0,10,5)
print(array)
print('=======')

# 난수의 재연 (실행마다 결과 동일)
np.random.seed(7) # seed를 추가하면 결과값은 동일
print(np.random.randint(0,10,(2,3))) # 매회 결과값이 다름
print('=======')

# numpy 배열 객체 복사
array1 = np.arange(0,10)
array2 = array1.copy()
print(array2)
print('=======')

# 중복된 원소 제거
array3 = np.array([1,1,1,1,1,3,3,3,3,4,4,4,4])
print(np.unique(array3))

