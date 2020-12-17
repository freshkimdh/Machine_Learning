# 1. 리스트 생성
list1 = ['a', 'b', 'c', 'd', 'f', 'g']

print(list1[0])
print(list1[-1])

# 2. 리스트 수정
list2 = ['a', 'b', 'c', 'd', 'f', 'g']
list3 = list2 + [1]

print(list3)

list4 = [1,2,3]
list5 = [4,5,6]

print(list4 + list5)

# 3. 리스트 삭제
del(list4[0]) # 인덱스 삭제
print(list4)

list4.remove(3) # 인덱스의 값 삭제
print(list4)


# 4. if문 활용
number = [1,2,3,4,5]
if 5 in number : 
    print('5가 있다')