
def random_res(): # 함수
    "무작위로 가위바위보를 낸다"
    import random # 모듈
    return random.choice(['가위', '바위', '보'])

print(random_res())


