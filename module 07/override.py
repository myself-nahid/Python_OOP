class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('vat mangso polau korma')

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)
    
    # Override
    def eat(self):
        print('Vegetables')

    # + sign operator overload
    def __add__(self, others):
        return self.age + others.age

    # * sign operator overload
    def __mul__(self, others):
        return self.age * others.age

    def __len__(self):
        return self.height

shakib = Cricketer('Shakib Al Hasan', 38, 68, 90, 'BD')
mushi = Cricketer('Mushfiqur Rahim', 36, 58, 80, 'BD')
# shakib.eat()

# Plus sign overload
print(shakib + mushi)
print(shakib * mushi)
print(len(shakib))
