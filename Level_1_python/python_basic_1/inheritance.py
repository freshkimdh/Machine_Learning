class Animal():
    def walk(self):
        print('걷는다')
    def eat(self):
        print('먹는다')

class Human(Animal):
    # def walk(self):
    #     print('걷는다')
    # def eat(self):
    #     print("먹는다")
    def wave(self):
        print('손을 흔든다.')

class Dog(Animal):
    # def walk(self):
    #     print('걷는다')
    # def eat(self):
    #     print("먹는다")
    def wag(self):
        print('꼬리를 흔든다.')

person = Human()
person.walk()
person.eat()
person.wave()

dog = Dog()
dog.walk()
dog.eat()
dog.wag()

