fruits = ["orange", "mango", "banana", "apple", "guava"]
vegetables = ["onion", "chilli", "ginger", "potato"]

in_val = input("Enter a vegetable or fruit: ")

if in_val in fruits:
    print("It is a fruit")
elif in_val in vegetables:
    print("It is a vegetable")
else:
    print("To my knowledge, I don't know what it is.. Sorry")