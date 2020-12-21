# 평균 제곱의 오차
import numpy as np

# 원소는 첫번째 인덱스부터 0,1,2 ... 9 되어있다.

# t 는 정답을 가리키는 원소로 숫자'2' 1로 하고 나머지는 0
# 한 원소만 1로 하고 그 외는 0으로 표기하는 법을 '원-핫 인코딩'
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0] # 정답은 2

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

# '0'일 확률 0.1, '2'일 확률 0.05
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
result = mean_squared_error(np.array(y), np.array(t))
print("y1 = ",result) # 2일 오차 확률을 추정

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
result = mean_squared_error(np.array(y), np.array(t))
print("y2 = ",result) # 7일 오차 확률을 추정

# 정답은 '2' 인데,
# 결과값은 y1 이 오차가 적으니, 2가 정답이라고 맞춤