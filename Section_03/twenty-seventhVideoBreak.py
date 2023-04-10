letters = "abcdefg"
guess = " "

while guess not in letters:
    guess = input("Guess a letter: ")
    if guess == "Key":
        break

print("Well Done!")