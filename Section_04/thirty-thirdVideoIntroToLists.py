#name = ["Alex", "Abdul", "David", "Mary"]

"""for i in name:
    print(i)
print(name[1])

print(name[2:5])
print(name)"""
#add to list
'''print(name)
name.append("Stephan")
print(name)
name += ["Saad","Mustafa"]
print(name)
name.insert(2,"Chritian")
print(name)'''

#min, max, len()

'''num = [1,2,3,1,2,7,9,6,9,0,0,4,2]

print(min(num))
print(max(num))
print(num.count(3))
print("country".count("t"))
print(len(num))

name = "Big table"
print(len(name))
'''

#enumerate

'''for index, name in enumerate("abcdefg"):
    print(index,name)



meals = ["Chicken", "Rice", "Beef"]
for  meal in meals:
    print(meal)

for number, meal in enumerate(meals):
    print(number +1, meal)'''

#list challenge

'''print("1- Phone")
print("2- computer")
print("3- Printer")
print("4- TV")
print("0- Exit")
# my solution'''

'''user_input = " "

while  user_input != "0":

    user_input = int(input("Enter a number: "))
    if user_input == 0:
        print("0- Exit")
        break

    elif user_input == 1:
        print("1- Phone")
        break
#
    elif user_input == 2:
        print("2- computer")
        break

    elif user_input == 3:
        print("3- Printer")
        break

    elif user_input == 4:
        print("4- TV")
        break '''

    # the instructor's solution

'''user_list = []
user_choice =" "
while user_choice != '0':
    if user_choice in "1234":
        if user_choice == "1":
            user_list.append("Phone")
            print("Phone is added to list")
        elif user_choice == "2":
            user_list.append("Computer")
            print("Computer is added to list")
        elif user_choice == "3":
            user_list.append("Printer")
            print("Printer is added to list")
        elif user_choice == "4":
            user_list.append("TV")
            print("TV is added to list")
    else:
        print("1- Phone")
        print("2- computer")
        print("3- Printer")
        print("4- TV")
        print("0- Exit")

    user_choice = input(": ")

print(user_list)'''

#challenge 2

'''user_list = []
user_choice =" "
while user_choice != '0':
    if user_choice in "12345":
        if user_choice == "1":
            user_list.append("Phone")
            print("Phone is added to list")
        elif user_choice == "2":
            user_list.append("Computer")
            print("Computer is added to list")
        elif user_choice == "3":
            user_list.append("Printer")
            print("Printer is added to list")
        elif user_choice == "4":
            user_list.append("TV")
            print("TV is added to list")
        elif user_choice == "5":
            user_list.append("PlayStation 5")
            print("PlayStation 5 is added to list")
    else:
        print("1- Phone")
        print("2- computer")
        print("3- Printer")
        print("4- TV")
        print("5- PlayStation 5")
        print("0- Exit")

    user_choice = input(": ")

print(user_list)'''
available_products = ["Phone", "Computer", "Printer", "TV" ,"PS5", "cable"]
user_list = []
user_choice =" "
while user_choice != '0':
    if user_choice in "12345":
        if user_choice == "1":
            user_list.append("Phone")
            print("Phone is added to list")
        elif user_choice == "2":
            user_list.append("Computer")
            print("Computer is added to list")
        elif user_choice == "3":
            user_list.append("Printer")
            print("Printer is added to list")
        elif user_choice == "4":
            user_list.append("TV")
            print("TV is added to list")
        elif user_choice == "5":
            user_list.append("PlayStation 5")
            print("PlayStation 5 is added to list")
    else:
        for number, product in enumerate(available_products):
            print(f"{number + 1}: {product}")


    user_choice = input(": ")

print(user_list)