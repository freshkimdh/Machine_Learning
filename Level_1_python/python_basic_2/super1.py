#super

class Car():
    def __init__(self, name):
        self.name = name
    def run(self):
        print("{} 차가 달립니다.".format(self.name))

class Truck(Car):
    # 이 아래에서 __init__ 메소드를 오버라이드 하세요.
    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity
    def load(self):
        super().run()
        print("{} 짐을 실었습니다".format(self.capacity))

truck = Truck("코나", 10)
truck.run() 
truck.load()
