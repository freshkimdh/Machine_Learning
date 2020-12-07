# 3. 텍스트 안에 단어에 id를 부여하고 각 단어의 빈도수를 세어
# 각각의 텍스트에 해당하는 id를 저장하는 딕셔너리와 (o)

# 각각의 단어 id에 해당하는 빈도수를 저장하는 딕셔너리 리턴

# 텍스트 안에 특수 기호는 제거해야한다 (o)
# 모든 단어는 소문자 형태로 관리한다 (o)

# id_dict  = { Apple : 0 , is : 1,} 
# count_dict = { 0 : 1 , 1 : 3 }

import re
import collections

def word_index_count(text):

    #소문자 변환
    lower_text = text.lower()

    #특수문자 제거
    re_lower_text = re.sub('[.?]', '',lower_text)

    #단어 split
    split_text = re_lower_text.split(' ')

    #id 부여
    word_id = {
    0 : split_text[0], 1 : split_text[1], 2 : split_text[2],
    3 : split_text[3], 4 : split_text[4], 5 : split_text[5],
    6 : split_text[6], 7 : split_text[7], 8 : split_text[8],
    9 : split_text[9]
    }

    id_frequency = {}

    return word_id, id_frequency


text = "Apple is fruit. Orange is also fruit. Tomato is fruit?"
print(word_index_count(text))