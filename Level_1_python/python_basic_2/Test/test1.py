# 1. "dk2jd923i1jdk2jd93jfd92”의 길이를 구하세요.
a = "dk2jd923i1jdk2jd93jfd92”의"
print(len(a))


# 2.  t1 = 'python’, t2 = 'java’일 때 문자열 더하기와 곱하기를 이용하여 ”python java python java python java”를 출력 하세요.
t1 = 'python'
t2 = 'java'

t3 = t1 + " " + t2 + " " + t1 + " " + t2 + " " + t1 + " " + t2 + " "
print(t3)

# t1 = ' python java '
# print(t1 * 3)

# # 3. id = "890910-1157963"에서 성별을 나타내는 수를 출력하세요.
# id = "890910-1157963"

# if id[8] == '1' :
#     print('남자')
# elif id[8] == '2' :
#     print('여자')
# else :
#     print('오류 입니다.')


# # 4. license_plate = "24가 2210”에서 번호판 뒷자리만 출력하세요.
# license_plate = '24가 2210'
# print(license_plate[4:])


# # 5. url =peoplei.kr 에서 kr만 출력하세요. (split 함수 사용)
# url = 'peoplei.kr'
# str = url.split(".")
# print(str[1])


# # 6. language1 = ["C", "C++", "JAVA"], language2 = ["Python", "Go", "C#"] 두 리스트의 원소를 모두 갖는 languages를 만드세요.
# language1 = ["C", "C++", "JAVA"]
# language2 = ["Python", "Go", "C#"]

# languages = language1 + language2.
# print(languages)


# 7.nums = [12, 245, 33, 77, 858]의 평균을 구하세요.
nums = [12, 245, 33, 77, 858]
sum = 0

for i in range(len(nums)) :
    sum = sum +nums[i]

average = sum/len(nums)
print(average)


# 8. a = ["b", "a", "d", "c"] 리스트를 알파벳 순으로 정렬하세요.
a = ["b", "a", "d", "c"]
a.sort()
print(a)
