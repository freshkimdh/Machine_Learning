class Animal():
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('걷는다')
    def eat(self):
        print('먹는다')
    def greet(self):
        print('{}이/가 인사한다'.format(self.name))

class Human(Animal):
    def __init__(self, name, hand):
        super().__init__(name)
        self.hand = hand

    def wave(self):
        print('{}을 흔들면서'.format(self.hand))
    def greet(self): # override 자식이 구현해라
        self.wave()
        super().greet()

person = Human('사람', '오른손')
person.greet()


class Car():

    def __init__(self, name):
        self.name = name

    def run(self):
        print("차가 달립니다.")


class Truck(Car):
    # 이 아래에서 __init__ 메소드를 오버라이드 하세요.
    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity

    def load(self):
        print("{}의 {}가 짐을 실었습니다".format(self.name, self.capacity))


truck = Truck("코나", 10)
truck.load()