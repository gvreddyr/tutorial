expenses = [6100, 6500, 5200, 8000, 6500, 7100]
# total_expenses = expenses[0] + expenses[1] + expenses[2] + expenses[3] + expenses[4] + expenses[5]
total_expenses = 0

for elem in expenses:
    total_expenses = elem + total_expenses

print("My expenses so far: ", total_expenses)