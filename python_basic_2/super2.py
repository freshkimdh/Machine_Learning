class Animal():
    def __init__(self, name):
        self.name = name
    def walk(self):
        print('걷는다')
    def greet(self):
        print('{}가/이 인사한다.'.format(self.name))

class Human(Animal):
    def __init__(self, name, hand):
        super().__init__(name) 
        self.hand = hand
    def wave(self):
        print('{}을 흔들면서'.format(self.hand))
    def greet(self): #오버라이드
        self.wave()
        super().greet()

person = Human('사람', '오론손')
person.greet()
    

