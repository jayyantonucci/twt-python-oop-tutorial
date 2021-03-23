
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def speak(self):
        print(self.name, 'is BORKING')

    
    def change_age(self, age):
        self.age = age
        print(f'{self.name}: Actually I am {self.age} years old...')


    def greet(self):
        print(f'{self.name}: Hello! My name is {self.name} and I am {self.age} year(s) old!')


    def add_weight(self, weight):
        self.weight = weight

molly = Dog('Molly', 1)
sako = Dog('Sako', 5)


molly.speak()
sako.speak()
molly.greet()
sako.greet()
sako.change_age(6)

print(molly.name, molly.age)
print(sako.name, sako.age)

molly.add_weight(70)
print(molly.weight)