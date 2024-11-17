try: 
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Invalid input")
    exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Can't divide by zero.")
    exit(1)

print(f"{x} / {y} is equal to {result}")