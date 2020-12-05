class Animal():
    def walk(self):
        print('걷는다')
    def eat(self):
        print('먹는다')
    def greet(self):
        print('인사한다')

class Human(Animal):
    def wave(self):
        print('손을 흔든다.')
    def greet(self): # override 자식이 구현해라
        self.wave()

class Dog(Animal):
    def wag(self):
        print('꼬리를 흔든다.')
    def greet(self): # override 자식이 구현해라
        self.wag()

person = Human()
person.greet()

dog = Dog()
dog.greet()

