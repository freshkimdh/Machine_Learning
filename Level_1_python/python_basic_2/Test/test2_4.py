#4. 별트리 그리기
#     *
#    ***
#   *****
#  *******
# *********

# format 활용
for i in range(1, 11, 2): # (시작숫자, 종료숫자, step)
     print('{:^10}'.format('*' * i))

# 일반 for문 활용
for i in range(1,6):
    for j in range(5-i):
        print(' ',end="")
    for j in range(1,i*2,1):
        print('*',end="")
    print('')