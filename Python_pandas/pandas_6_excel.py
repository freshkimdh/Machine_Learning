import pandas as pd

word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근'
}

frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': 7
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)

summary = pd.DataFrame({
    'word': word,
    'frequency': frequency
})

# 엑셀로 내보내기
summary.to_csv("summary.csv", encoding="utf-8-sig")
# 엑셀 파일 불러오기
saved = pd.read_csv("summary.csv", index_col=0)
print(saved)