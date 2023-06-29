def add_marks(**kwargs):
    total_marks = 0
    for marks in kwargs.values():
        total_marks += marks
    return total_marks


d = {
    'maths': 70,
    'telugu': 80,
    'social': 75,
    'science': 81,
    'hindi': 60
}

print(add_marks(**d))
