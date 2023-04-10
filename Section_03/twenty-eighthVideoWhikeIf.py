#my solution

'''answer = 10
guess = int(input("Enter a number: "))

while guess < answer:
    print("Guess Higher")
    guess = int(input("Enter a number: "))
while guess > answer:
    print("Guess lower")
    guess = int(input("Enter a number: "))

else:
    print("Well Done!")'''

#the instructor's solution

answer = 10
guess = 0


while guess != answer:
    guess = int(input("Enter a number: "))

    if guess < answer:
        print("Guess Higher")

    elif guess > answer:
        print("Guess lower")


    else:
        print("Well Done!")