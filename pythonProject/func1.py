def calculate_expenses(expenses):
    """
    This function calculates all the expenses from a given list of expenses

    :param expenses: list of expenses
    :return: returns total expenses
    """
    total_expenses = 0
    # iterate through all elements and calculate the expenses
    for elem in expenses:
        total_expenses = elem + total_expenses
    return total_expenses


john_expenses = [6100, 6500, 5200, 8000, 6500, 7100]
alex_expenses = [6200, 7500, 5600, 5000, 7500, 7100]
bob_expenses = [5200, 7800, 7600, 6000, 7500, 8100]


total_john_expenses = calculate_expenses(john_expenses)
print("John expenses so far: ", total_john_expenses)

total_alex_expenses = calculate_expenses(alex_expenses)
print("Alex expenses so far: ", total_alex_expenses)

total_bob_expenses = calculate_expenses(bob_expenses)
print("Bob expenses so far: ", total_bob_expenses)


