# class inheritance

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'{self.name}: BORK')

    def change_age(self, age):
        self.age = age
        print(f'{self.name}: Actually I am {self.age} years old...')

    def greet(self):
        print(
            f'{self.name}: Hello! My name is {self.name} and I am {self.age} year(s) old!')

    def add_weight(self, weight):
        self.weight = weight


class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(f'{self.name}: Meow!')


molly = Dog('Molly', 1)
sako = Dog('Sako', 5)
syd = Cat('Sydman', 8, 'white/brown')
fred = Cat('Freddie', 8, 'grey')

animals = [molly, sako, syd, fred]

for i in animals:
    i.speak()
    i.greet()
