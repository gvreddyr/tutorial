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



a = Animal(4, "black")
