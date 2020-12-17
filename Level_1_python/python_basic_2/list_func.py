# list의 다양한 기능

#value의 인덱스를 리턴하는 함수
def safe_index(my_list, value):
    if value in my_list:
        return my_list.index(value)
    else:
        return

print(safe_index([1,2,3,4,5], 5))
print(safe_index([1,2,3], 5))



list1 = [1, 2, 3, 4]

# 아래줄에서 list1의 1번째 자리에 8을 넣고 원래 있던 값은 오른쪽으로 밀어 보세요.
list1.insert(0,8)
print("첫 번째 자리에 8을 넣은 결과 : {}".format(list1))

# 아래줄에서 list1을 작은 수부터 큰 수로 정렬해 보세요
list1.sort()
print("list1을 작은 수부터 큰 수로 정렬한 결과 : {}".format(list1))

# 아래줄에서 list1을 거꾸로 만들어 보세요
list1.reverse()
print("list1을 거꾸로 정렬한 결과 : {}".format(list1))