import numpy as np

x = np.array([-1.0, 1.0, 2.0])
print("x 값",x)

# 넘파일 배열에 부등호 연산을 수행하면 bool 배열이 생성
y = x > 0
print("y 값",y)

y = y.astype(np.int)
print("int 형으로 변환",y)


