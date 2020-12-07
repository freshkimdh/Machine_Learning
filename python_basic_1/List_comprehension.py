#기존
areas1 = []
for i in range(1,11) :
    if i%2 == 0: #길이가 짝수인 사각형 넓이
        areas1 = areas1 + [i*i]
print("areas1: ", areas1)


#List comprehension
areas2 = [i*i for i in range(1,11) if i%2==0]
print("areas2: ", areas2)


#8의 배수
list1 = [i for i in range(1,100) if i%8==0]
print("list1 : ", list1)