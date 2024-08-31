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