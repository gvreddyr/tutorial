num = input("Enter a number: ")

num = int(num)

for i in range(2,num):
    if num%i == 0:
        print("It's not a prime number")
        break
else:
    print("It's prime number")