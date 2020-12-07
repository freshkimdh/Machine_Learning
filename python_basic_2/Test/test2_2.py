# #2. 특별반 학생의 리스트를 리턴하는 함수를 완성하세요 특별반은 점수가 80점 이상이어야 들어갈 수 있다.
# def get_special_students(student2score):

#     special_students = {}


    
#     #새로운 딕셔너리 생성이 필요
#     special_students = {key: value for key, value in student2score.items() if value >= 80} 
#     return special_students

#     # 아래와 같이 하면 안됨
#     # for key,value in student2score.items() :       
#     #     if value >= 80 :          
#     #         print(key, value)
#     #         special_students.append([key,value])
#     #         print(special_students)

# student2score = {
#     "people1": 100,
#     "peopleA": 80,
#     "people2": 60,
#     "kim": 75,
#     "hyeon": 20,
#     "jin": 97
# }

# print(get_special_students(student2score))

s = {"kim": 1, "hyeon" : 2 } 
s["jin"] = 3
print(s)