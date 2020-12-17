import numpy as np

x = np.array([0, 1])        # 입력
w = np.array([0.5, 0.5])   # 가중치
b = -0.7                    # 편향

# 퍼셉트론을 코드로 변환
# x1*w1 + x2*w2 > or <= theta
# theta를 b로 치환
# b + x1*w1 + x2*w2 > or <= 0

print(w*x)              # 입력 * 가중치
print(np.sum(w*x))      # 각 곱의 합
print(np.sum(w*x)+b)    # 세타가 치환된 편향 + b

