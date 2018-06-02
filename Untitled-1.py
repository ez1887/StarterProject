class Dog():
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def setName(self, name):
        self.name = name
    def getName(self):
        print(self.name)
    def bark(self):
        print("WOOF!")

rex = Dog("Rex", "Brown")
rex.getName()
rex.setName("Rexy Boy")
rex.getName()
rex.bark()
rex.bark()