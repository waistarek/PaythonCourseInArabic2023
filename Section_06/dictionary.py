#intro to Dictionary 
''' 
#list a = []
#tuple b = ()
#dictionary c = {}

#cars = {'key' : 'value', 'key2' : 'value2'}
cars = {
    '1010' : 'Ahmed Adam',
    '1011' : 'Muhammed Amin',
    '1012' : 'Turki Fahad',
    '1013' : 'Nawaf Rakan',
    '1014' : 'Saleh Othman',
}

name = cars['1011']
print(name)
'''

#get method

''' 
cars = {
    '1010' : 'Ahmed Adam',
    '1011' : 'Muhammed Amin',
    '1012' : 'Turki Fahad',
    '1013' : 'Nawaf Rakan',
    '1014' : 'Saleh Othman',
}
#a = cars['101']# if you want to access a value of a key that does exit you will get a error (KeyError: '101'). 
                #to avoid this error you can use the method get 
#print(a)

name = cars.get('101')
print(name)
'''

# items
''' 
cars = {
    '1010' : 'Ahmed Adam',
    '1011' : 'Muhammed Amin',
    '1012' : 'Turki Fahad',
    '1013' : 'Nawaf Rakan',
    '1014' : 'Saleh Othman',
}

# for key in cars:
#     print(key, cars[key] )
#for key in cars:
     #print(f"{key}, {cars[key]}" )
     #print()
     #print(key, cars[key], sep=", ")


for key, value in cars.items():# iterating a dictionary using items() is more efficient than the example above 
    print(key, value, sep=",   ")
'''

#add and change value
''' 
cars = {
    '1010' : 'Ahmed Adam',
    '1011' : 'Muhammed Amin',
    '1012' : 'Turki Fahad',
    '1013' : 'Nawaf Rakan',
    '1014' : 'Saleh Othman',
}
#add a value
cars['1015'] = "Salah Adam"
cars["1016"] = "Alex Mueller"

# change a value
cars["1010"] = "Abullah Abduaramhan" 

print(cars)

for key, value in cars.items():
    print(key, value, sep=", ")
'''
#del and pop 

''' 

cars = {
    '1010' : 'Ahmed Adam',
    '1011' : 'Muhammed Amin',
    '1012' : 'Turki Fahad',
    '1013' : 'Nawaf Rakan',
    '1014' : 'Saleh Othman',
}

del cars['1012'] # you can remove an entry using del if you sure that this key exists. If not you have to use pop()
delete = cars.pop("1010", "Not found")
print(delete)
for key, value in cars.items():
    print(key, value, sep=", ")
'''
#in
''' 
cars = {
    '1010' : 'Ahmed Adam',
    '1011' : 'Muhammed Amin',
    '1012' : 'Turki Fahad',
    '1013' : 'Nawaf Rakan',
    '1014' : 'Saleh Othman',
}

user = input(": ")
if user in cars:# here the value(user) is accessed 
    print(cars[user])
else:
    print("Key not found!")
'''

#items challenge

product = {
    "1" : "Shirt",
    "2" : "Jacket",
    "3" : "Pants",
    "4" : "Hat",
    "5" : "Shoes",
}

# my solution 
# print("Here are the available products")
# for key, value in product.items():
#     print(f"{key}- {value}") 
# userChoise = input(": ")
# user_cart={}
# #user_cart[1] = product["1"]
# for key in product.items():
#     if userChoise == key:
#         user_cart[userChoise] = product[key]


# # if int(userChoise) == 1:
# #     user_cart["1"] = "Shirt"

# print(user_cart)

#the instructor's solution 

cart = {}
user = "-"
while user != "0":
    if user in product:
        if user in cart:
            print("item already in your cart!")
        else:
            print(f"Adding {product[user]}")
            cart[user] = product[user]
            print(f"your cart now contains {cart}")
    else:
        for key, value in product.items():
            print(key,value, sep="- ")
        print("0: to exit")
    user = input(": ")
        