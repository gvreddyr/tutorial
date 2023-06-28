num = input("Enter a number: ")

num = int(num)

is_not_prime = False
i = 2
while i < num:
    if num % i == 0:
        print("It's not a prime")
        is_not_prime = True
        break
    i = i + 1

if not is_not_prime:
    print("It's a prime")