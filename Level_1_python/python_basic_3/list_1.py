# 정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. 
# solution 함수가 mylist 각 원소의 길이를 담은 리스트를 리턴하도록 코드를 작성해주세요.

list1 = [[1, 2], [3, 4], [5]]

def solution1(mylist):
    answer = []
    for i in mylist:
        answer.append(len(i))
    return answer

print(solution1(list1))


# def solution2(mylist):
#     return list(map(len, mylist))

# print(solution1(list1))