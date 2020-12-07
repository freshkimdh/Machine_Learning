
#상속
class Animal():
    def walk(self):
        print('걷는다')
    def eat(self):
        print('먹는다')

class Human(Animal):
    def wave(self):
        print('손을 흔든다')

class Dog(Animal):
    def wag(self):
        print('꼬리를 흔든다')

person = Human()
person.walk() # 상속을 받아서 출력 가능
person.wave()

dog = Dog()
dog.eat()
dog.wag()