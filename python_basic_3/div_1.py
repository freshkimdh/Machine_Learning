#숫자 a, b가 주어졌을 때 a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력해보세요.

# strip() 함수
# whitespace 를 제거 해준다. 띄어쓰기, 탭, 엔터 까지 포괄적으로 얘기 한다.

# map() 내장 함수
# map(변환 함수, 순회 가능한 데이터)

# divmod() 함수
# 나머지와 몫을 한번에 구할 수 있음
# 무조건 좋은 것은 아니며, 큰 숫자에서 유리 하다.

a, b = map(int, input().strip().split(' '))
print(a//b, a%b)
print(*divmod(a,b))

# str1 = '   11  a b c d  11  '
# print(str1.strip())