#intro to tuples 
'''
name = "a", "b", "c" # you could put the value in parentheses like ("a", "b", "cd")
print(name)

print(type(name)) # the output is : <class 'tuple'> 
''' 

# tuples vs lists
'''

#lists in Python are mutable 
name2 = ["a", "b", "c"]
name2[0] = "x"
print(name2) # output: ['x', 'b', 'c']
print('------------------------------------------------------')
#Tuples in Python are immutable 
name = "a", "b", "c"

name[0] = "x" # output: name[0] = "x"
                #       ~~~~^^^
                #TypeError: 'tuple' object does not support item assignment
print(name)
print("--------------------------------")
print(name[0]) # => indexing
print(name[1])
print(name[2])
'''
# more on tuples 
''' 

a = b = c = 100
print(a) # 100
print(b) # 100
print(c) # 100
print("-" * 50)
x, y, z = 1, 10, 100 

print(x) # 1
print(y) # 10
print(z) # 100

numbers = (20, 30, 40)

num1, num2, num3 = numbers
print(num1) # 20
print(num2) # 30
print(num3) # 40
'''

# unpacking a tuple example
''' 
land1 = ("House", 100, 150)
land2 = ("Shop", 200, 250)
land3 = ("Empty", 300, 300)


land_type, width, length = land1

area = width * length

print(area)
'''

#nested tuples 

''' 

cars = [
    ("Toyota", "Corolla", 2023),
    ("Hyundai", "Elantra", 2020),
    ("Kia", "K8", 2015),
    ("Ford", "Taurus", 2021),
   ("Nissan", "Maxima", 2018),  
]

print(len(cars))

# for car in cars:
#     print(car)
print("Company | name | year") 
for company, name, year in cars:
    print(f"{company}, {name}: {year}")
print("-" * 100)
for car in cars:
    company, name, year = car
    print(f" {company}, {name}, {year}")
'''

# indexing examples 
''' 

cars = (
    (("Toyota", "Japanese"), "Corolla", 2023),
    ("Hyundai", "Elantra", 2020),
    ("Kia", "K8", 2015),
    ("Ford", "Taurus", 2021),
   ("Nissan", "Maxima", 2018),  
)

print(cars[0][0][1])
''' 
# challenge
''' '''

names = (
    ("055555", 1990, "Ahmed"),
    ("066666", 1985, "muhmmed"),
    ("077777", 2002, "Rakan"),
    ("088888", 1979, "Ali"),
)
#my solution
'''
user_input = input("Enter your phone number: ")

for name in names:
    if(name[0] == user_input or name[2] == user_input):
         print(name[1])

'''
# the instructor's solution
choise = input(": ")
for index, value in enumerate(names):
     print(index, value)
     if choise == value[0] or choise == value[2]:
        a = index
        print(names[a][1])
        break
     
     continue
    
