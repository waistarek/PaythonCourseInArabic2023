answer = 10

guess = int(input("Enter a number: "))

if guess < answer:
    print("Guess higher")
elif guess > answer:
    print("Guess lower ")
else:
    print("Correct guess")
