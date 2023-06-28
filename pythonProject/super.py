class Super:
    __super_prop = 0
    def __init__(self, s):
        self.__super_prop = s

    def my_actions1(self):
        print("I super work for %d days"%self.__super_prop)

class Sub(Super):
    _sub_prop = 0
    def __init__(self, sub_s, super_s):
        self._sub_prop = sub_s
        super().__init__(super_s)

    def my_actions(self, night=False):
        print("I work for %d days"%self._sub_prop)
        if night:
            print("I do work at night also")

    def __print_props(self):
        print(self._sub_prop)

    def print_props(self):
        self.__print_props()


s = Sub(5,1)
s.my_actions1()
s.my_actions(True)
s.print_props()
print(s._sub_prop)


#s.print_props()
