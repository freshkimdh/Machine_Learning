import numpy as np

# np.amax()
array1 = np.random.randint(0, 10, (3,3))
print(array1)
print("amax",np.amax(array1))

# np.nonzero - 1
array2 = np.array([0,2,3]) # 0 이 아닌 인덱스 값을 출력
print("nonzero",np.nonzero(array2))

# np.nonzero - 2
array3 = np.array([[1,0,2,4],[0,0,2,1]])

a = array3[1]
print("nonzero",np.transpose(np.nonzero(array3)))
print(a)



