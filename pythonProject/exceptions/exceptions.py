print("I'm at the begin watching everything")
x = 10
try:
    x = x // 0
except Exception as e:
    print("I got an exception:", e)
finally:
    print(f"X value is {x}")

print("I'm at the end watching everything")