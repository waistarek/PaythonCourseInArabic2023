answer = 10

guess = int(input("Enter a number: "))

if guess < answer:
    print("Guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done")
    else:
        print("wrong answer")
elif guess > answer:
    print("Guess lower ")
    guess = int(input())
    if guess == answer:
        print("Well done")
    else:
        print("wrong answer")
else:
    print("Correct guess")