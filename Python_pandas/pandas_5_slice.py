import pandas as pd

word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근',
    'Durian': '두리안'
}

frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': 7,
    'Durian': 2
}

importance_dict = {
    'Apple': 3,
    'Banana': 2,
    'Carrot': 1,
    'Durian': 1
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)
importance = pd.Series(importance_dict)

summary = pd.DataFrame({
    'word': word,
    'frequency': frequency,
    'importance': importance
})

print(summary)

# 이름을 기준으로 슬라이싱
print(summary.loc['Banana':'Carrot', 'importance':])

# 인덱스를 기준으로 슬라이싱
# lioc[x:y, a:b]
# x:y 는 x 이상 y 미만 (열기준)
# a:b 는 "2:" 인덱스 2부터 가져온다는 것 
print(summary.iloc[1:3, 2:])