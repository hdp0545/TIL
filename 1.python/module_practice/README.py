class Dog(Animal):
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 달린다!')

    def run(self):
        print(f'{self.name}! 달린다!')

class Bird(Animal):
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f'{self.name}! 푸드덕!')