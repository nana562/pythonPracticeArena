class Point:
    def __init__(self, x, y):  # constructor
        self.x = x
        self.y = y

    def move(self):  # methods
        print('move')

    def draw(self):
        print('draw')


point = Point(1, 19)

print(point.y)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):  # methods
        print(f'Hi, I am {self.name}')


john = Person("Gideon")
john.talk()

bob = Person("Father Burgess")
bob.talk()



