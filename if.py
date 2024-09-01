cars = ['audi' , 'bmw' , 'toyota' , 'tata']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())    

requested_toppings = 'mushrooms'
if requested_toppings != 'capsicum':
    print("Hold the capsicum")

car = 'bmw'    
if car == 'bmw':
    print('True')

age = 18
if age == 18:
    print('True')

answer = 17
if answer != 42:
    print("That is not correct answer. Please try again!")   

age = 19
if age < 21:
    print('True')
if age <= 21:
    print('True')    
if age > 21:
    print('False')    
if age >= 21:
    print('False')    

age_0 = 22
# age_1 = 18
age_1 = 21
if age_0 >= 21 and age_1 >= 21:
    print('True')
else:
    print('False') 

# age_2 = 22
age_2 = 18
age_3 = 18
if age_2 >= 21 or age_3 >= 21:
    print('True')   
else:
    print('False')

topping = ['onion' , 'olives' , 'cheese']
if 'onion' in topping:
    print('true')
if 'capsicum' in topping:
    print('false')

users = ['adi' , 'sam' , 'dev']
user = 'marie'
if user not in users:
    print(user.title() + ", You can post a response.")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, You are too young to vote.")    
    print("Please register as soon as you turn 18!")

age = 12
if age < 4:
    print("Your admission cost is 0$") 
elif age < 18:
    print("Your admission cost is 5$")
else:
    print("Your admission cost is 10$")

age = 66
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")

toppings = ['cheese' , 'corn']
if 'cheese' in toppings:
    print("Adding cheese.")
if 'mushroom' in toppings:
    print("Adding mushroom.")
if 'corn' in toppings:
    print("Adding corn.")
print("\nFinished making your pizza.")

topping = ['mushroom' , 'corn' , 'cheese']
for topping in topping:
    if topping == 'corn':
        print("Sorry we are out of corn right now.")
    else:
        print("Adding " + topping + ".")
print("\nFinished making your pizza.")

toppings = []
if toppings:
    for topping in toppings:
        print("Adding " + topping + ".")
    print("\nFinished making your pizza.")
else:
    print("Are you sure you want a plane pizza?")

available = ['corn' , 'cheese' , 'capsicum' , 'mushroom' , 'pepper']
requested = ['cheese' , 'french fries' , 'capsicum']
for requested in requested:
    if requested in available:
        print("Adding " + requested + ".") 
    else:
        print("Sorry we don't have " + requested + " right now.")
print("\nFinished making your pizza.")

