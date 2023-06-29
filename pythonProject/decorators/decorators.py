def greetings(f):
    def inner():
        print("Hi!!")
        f()
        print("Bye!!")
    return inner
@greetings
def my_name():
    print("Govardhan")


my_name()