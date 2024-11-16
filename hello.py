print("hello world")

name = input("Enter your name: ")

print(f"hello, {name}")

age = int(input("Enter your age: "))

if age > 18:
    print(f"{name}'s {age} is greater than 18")
else:
    print(f"{name}'s age is {age}")

my_name = "AbdulSalam"

print(my_name[5])

names = ["alex", "jhon", "david"]

names.append("harry")
names.sort()

print(names[0])
print(names[1])

cordinate = (12, 34)

for name in names:
    print(name)

houses = {
    "alex": "gryffindor",
    "harry": "slytherin"
}

houses["adam"] = "gryffindor"

print(houses["alex"])

def square(x):
    return x * x

for i in range(1, 11):
    print(f"the square of {i} is {square(i)}")