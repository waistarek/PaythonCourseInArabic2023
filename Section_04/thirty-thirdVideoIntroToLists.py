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

'''
user_input = " "

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
''' 
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
        print("1- Phone")
        print("2- computer")
        print("3- Printer")
        print("4- TV")
        print("5- PlayStation 5")
        print("0- Exit")

    user_choice = input(": ")

print(user_list) 
'''
''' 
available_products = ["Phone", "Computer", "Printer", "TV" ,"PS5", "Cable", "Desk", "Chair"]
user_list = []
user_choice = " "
valid_options = []
for i in range(1,len(available_products) + 1):
    valid_options.append(str(i))
print(valid_options)

while user_choice != '0':
    if user_choice in valid_options:
        print(f"{available_products[int(user_choice) - 1]} is added")
        index = int(user_choice) - 1
        chosen_product = available_products[index]
        user_list.append(chosen_product)
    else:
        for number, product in enumerate(available_products):
            print(f"{number + 1}: {product}")


    user_choice = input(": ")

print(user_list)
    '''
#remove 

'''available_products = ["Phone", "Computer", "Printer", "TV" ,"PS5", "Cable", "Desk", "Chair"]
print(available_products)
available_products.remove("TV")
print(available_products)'''

''' 
available_products = ["Phone", "Computer", "Printer", "TV" ,"PS5", "Cable", "Desk", "Chair"]
user_list = []
user_choice = " "
valid_options = []
for i in range(1,len(available_products) + 1):
    valid_options.append(str(i))
print(valid_options)

while user_choice != '0':
    
    if user_choice in valid_options:
        #more features
       
        index = int(user_choice) - 1
        chosen_product = available_products[index]
        if chosen_product in user_list:
            print(f"{available_products[int(user_choice) - 1]} is already in your cart")
            
        else:
            print(f"{available_products[int(user_choice) - 1]} is added")
            user_list.append(chosen_product)
        print(f"Your current list is: {user_list}")
    else:
        for number, product in enumerate(available_products):
            print(f"{number + 1}: {product}")


    user_choice = input(": ")

print(user_list)
'''

#sort + extend
'''
num1 = [10, 30, 50, 70]
num2 = [20, 40, 60, 80]

num1.extend(num2)

print(num1)

num1.sort()

print(num1)

num1.sort(reverse = True)

print(num1)
 '''

''' 
# sort + extend 2
num1 = [10, 30, 50, 70]
num2 = [20, 40, 60, 80]

num1.extend(num2)

print(num1)

num1.sort() # this function list.sort() alerts the orginal list     

print(num1)
new_list = sorted(num1) # this fuction sorted(list) creates a new list 
print(new_list)

greeting = "Hello everyone"

# greeting.sort() you can not use this function to sort string 
print(greeting)

new = sorted(greeting) # you can use the function sorted(list) to sort a string because this function makes a copy from
# of the list 
print(new )
# output is a new sorted list : [' ', 'H', 'e', 'e', 'e', 'e', 'l', 'l', 'n', 'o', 'o', 'r', 'v', 'y']
print()

animals = ["Zoo", "Lion", "Mouse", "Monkey"]
print(animals)
animals.sort()
print(animals)

print()

new_animals = sorted(animals)

print(new_animals)
'''

# replacing value in list
'''
animals = ["Zoo", "Lion", "Mouse", "Monkey"]

print(animals)
animals[2] = "Tiger"
print(animals) 

'''

#del
 
'''
numbers = [100, 500, 200, 900, 300, 800, 400, 700, 1000, 600]
#print(numbers)
#numbers.remove(200)
#print(numbers)

#print(numbers)

#del numbers[2]
#print(numbers)

numbers.sort()
print(numbers)
max_num = 500
for index, value in enumerate(numbers):
   # print(index, value)
   if value > max_num:
      stop = index
      break
print(numbers[:stop])
'''
# nested list
''' 
countries = [
    ["Saudi Arabia", "Riyadh", "Asia"],
    ["Egypt", "Cairo", "Africa"], 
    ["United Arab Emirates", "Abu Dhabi", "Asia"],
    ["Algeria", "Algeria", "Africa"],
    ]

for country in countries:
    if "Asia" not in country:
        print(country)
'''

#split

word = "cats like to eat fish"

#new_list = word.split()
#print(new_list)

user = input(": ")
new_list = user.split()
print(new_list)
