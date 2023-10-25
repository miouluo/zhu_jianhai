# 定义 Animal 类
class Animal:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
    def eat(self):
        print(f"{self.name} is eating.")
    def talk(self):
        print(f"{self.name} is talking.")
# 定义 Dog 类，继承 Animal 类
class Dog(Animal):
    def __init__(self, name, weight, height, breed):
        super().__init__(name, weight, height)
        self.breed = breed
    def eat(self):
        print(f"{self.name} is eating bones.")
    def talk(self):
        print(f"{self.name} is barking.")
# 定义 Cat 类，继承 Animal 类
class Cat(Animal):
    def __init__(self, name, weight, height, color):
        super().__init__(name, weight, height)
        self.color = color
    def eat(self):
        print(f"{self.name} is eating fish.")
    def talk(self):
        print(f"{self.name} is meowing.")
# 定义 Bird 类，继承 Animal 类
class Bird(Animal):
    def __init__(self, name, weight, height, wingspan):
        super().__init__(name, weight, height)
        self.wingspan = wingspan
    def eat(self):
        print(f"{self.name} is eating seeds.")
    def talk(self):
        print(f"{self.name} is chirping.")
# 创建动物列表
animals = [Dog("Dog 1", 30, 60, "Golden Retriever"),
           Cat("Cat 1", 10, 30, "White"),
           Dog("Dog 2", 20, 40, "Bulldog"),
           Bird("Bird 1", 5, 20, 30),
           Dog("Dog 3", 15, 35, "Poodle")]
# 循环调用所有动物的吃和说话方法
for animal in animals:
    animal.eat()
    animal.talk()