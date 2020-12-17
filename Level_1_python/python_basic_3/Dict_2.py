#아래의 상품 딕셔너리 데이터를 가격에 따라 내림차순으로 정렬하는 프로그램을 작성하십시오.
# "TV": 200,
# "냉장고": 150,
# "책상": 35,
# "노트북": 120,
# "가스레인지": 20,
# "세탁기": 100

import operator

dic = {"TV": 200,
    "냉장고": 150,
    "책상": 35,
    "노트북": 120,
    "가스레인지": 20,
    "세탁기": 100
    }

dic = dict(sorted(dic.items(), 
        key=operator.itemgetter(1),
        reverse=True))

for key, value in dic.items():
   print("{}: {}".format(key, value))