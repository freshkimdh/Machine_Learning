import numpy as np

# numpy 합
a = np.random.randint(0,10, (2,2))
b = np.arange(2).reshape(1,2)

c = np.concatenate((a,b), axis=0)

# 형태 바꾸기

x = np.arange(6).reshape(2,3)

print(x)



# 행렬 형태로 만든 후 배열 세로로 합치기
# axis?? => basic_5 에서 진행



