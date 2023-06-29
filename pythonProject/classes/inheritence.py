class Animal:
    legs = 0
    color = None

    def __init__(self, l, c):
        self.legs = l
        self.color = c

    def i_shout(self):
        print("I shout")

    def my_color(self):
        print("My color is: ", self.color)

    def i_am(self):
        print("My number of legs are: ", self.legs)
        self.my_color()

class Dog(Animal):
    def my_name(self):
        print("I'm a dog")

    def i_shout(self):
        print("Bow bow!!")

d = Dog(4, "white")
print(d.legs, d.color)
d.my_name()
d.i_shout()
d.i_am()

class Shitzu(Dog):
    """Animal->Dog->Shitzu==> multi level"""
    def i_eat(self):
        print("I eat home food")

s = Shitzu(4,"black and white")
s.i_eat()
s.my_name()
s.i_shout()