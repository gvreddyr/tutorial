class A:

    def a(self):
        print("I'm in A's a method")

    def ab(self):
        print("I'm in class A's ab method")


class B:
    def b(self):
        print("I'm in B's b method")

    def ab(self):
        print("I'm in class B's ab method")


class C(A, B):
    # MRO - Method resolution order -- left to right
    pass


c = C()
c.a()
c.b()
c.ab()
