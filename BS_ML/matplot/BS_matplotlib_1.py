import numpy as np
# 그래프 그리기 위한 lib
import matplotlib.pyplot as plt

# 데이터 준비
x = np.arange(0, 6, 0.1) # 0에서 6까지 0.1 간격으로
y = np.sin(x)

# 그래프 그리기
plt.plot(x, y)
plt.show()
