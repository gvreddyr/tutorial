num = input("Enter a value: ")

num = int(num)

if num % 3 == 0 and num % 5 == 0:
    print("pet")
elif num % 3 == 0:
    print("bow")
elif num % 5 == 0:
    print("meow")
else:
    print("I dont know!!")
