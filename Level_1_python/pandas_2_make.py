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

# 이름(Name): 값(Values)
summary = pd.DataFrame({
    'word': word,
    'frequency': frequency
})

print(summary)

