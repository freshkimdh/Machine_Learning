import pandas as pd

# series 데이터 
# series 는 값과 index로 이루어져 있음
array = pd.Series(['사과','바나나','당근'], index=['a','b','c'])

print(array)
print(array['a']) # 특정 index의 값
