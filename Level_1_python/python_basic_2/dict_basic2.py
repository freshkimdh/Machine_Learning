ages = {
    'tod':35,
    'jane':23,
    'paul':62
}

#for key in ages: #생략가능
for key in ages.keys():
    print('{}의 나이는 {} 입니다.'.format(key,ages[key]))

# for value in ages.values() :
#     print(value)

for key,value in ages.items():
    print('{}의 나이는 {} 입니다.'.format(key,value))

#딕셔너리는 순서가 보장되지 않는다.
#대신 key를 가지고 값을 찾을수 있다는 장점

#순서가 중요한것은 list 사용해야 된다.
