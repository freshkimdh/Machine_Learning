#1. 홀수, 짝수를 구분하는 함수를 작성하세요.
def num_func(number):
    if number % 2 == 0 :
        print('짝수 입니다.')
    elif number % 2 == 1:
        print('홀수 입니다.')
    else :
        print('오류 입니다.')

num_func(24)