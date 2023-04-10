'''print("1:\tSaudi Arabia")
print("2:\tEgypt")
print("3:\tIraq")
print("0:\tExit")

#my solution
userInput = 4

while userInput != 0 or userInput != 1 or userInput != 2 or userInput != 3:
    userInput = int(input("Enter please a number: "))

    if userInput == 0:
        print("Exit")
        break
    if userInput == 1:
        print("Riyadh")
        break
    if userInput == 2:
        print("Cairo")
        break
    if userInput == 3:
        print("Bagdad")
        break'''
#the instructor's solution
print("1:\tSaudi Arabia")
print("2:\tEgypt")
print("3:\tIraq")
print("0:\tExit")

while True:
    user_input = int(input("Please enter a number: "))

    if user_input == 1:
        print("Riyadh")
    elif user_input == 2:
        print("Cairo")
    elif user_input == 3:
        print("Baghdad")
    elif user_input == 0:
        print("Riyadh")
        break

    else:
        print("Try again")