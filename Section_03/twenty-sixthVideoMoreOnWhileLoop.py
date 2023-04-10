letters = "abcdefg"
guess = " "

while guess not in letters:
    guess = input("Guess a letter: ")
    print("try again")

print("Well Done!")