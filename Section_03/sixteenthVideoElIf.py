name = input("Please enter your name: ")
age = int(input(f"Enter your age {name}!: " ))

if age < 18:
    print("\"You are under age\"")
elif age > 150:
    print("Invalid number")
elif age == 100:
    print("You are too old")
else:
    print("You are an adult")
