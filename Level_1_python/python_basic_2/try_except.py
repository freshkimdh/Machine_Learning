school = {'1반' : [172, 145, 184, 195, 192], '2반':[168, 177, 185, 194, 166]}

try:
    for class_number, height in school.items() :
        for i in height:
            if i>190:
                print(class_number,'반에 190을 넘는 학생이 있습니다.')
                raise StopIteration
except StopIteration :
    print('정상종료')


