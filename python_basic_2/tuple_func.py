ages = {'a':20, 'b':30, 'c':40}

for i in ages.items() :
    print('{}의 나이는 {} 입니다.'.format(*i))

for k,v in ages.items() :
    print('{}의 나이는 {} 입니다.'.format(k,v))