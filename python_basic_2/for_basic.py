# 1. for 기본
list1 = [1,2,3,4,5]

for i in list1 :
    print(i)

# 2. 구구단
for i in range(1,9):
    for j in range(1,9):
        result = i * j
        print('{} * {} = {}'.format(i,j,result))

# 3. for문 length
days = [31,29,31,30]

for i in range(len(days)):
    day = days[i]
    print('{}월의 날짜수는 {}일 입니다.'.format(i+1, day))
