import numpy as np

# numpy 파일 저장
array = np.arange(0,10)
np.save('saved1.npy', array)

# numpy 파일 불러오기
result = np.load('saved.npy')
print(result)
print('=======')

# 복수 객체 저장 및 불러오기
array1 = np.arange(0,10)
array2 = np.arange(10,20)
np.savez('saved2.npz', array1=array1, array2=array2)

data = np.load('saved2.npz')
result1 = data['array1']
result2 = data['array2']

print(result1)
print(result2)
