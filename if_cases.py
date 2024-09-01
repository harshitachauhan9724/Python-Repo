car = 'ferrari'
print("Is car == ferrari? I predict true.")
print(car == 'ferrari')
print("Is car == audi? I predict false.")
print(car == 'audi')

alien = 'green'
if alien == 'green':
    print("You just earned 5 points.")

alien = 'red'
if alien == 'green':
    print("You just earned 5 points.")

alien = 'green'
if alien == 'green':
    print("You just earned 5 points.")
elif alien == 'red':
    print("You just earned 10 points.") 
elif alien == 'yellow':
    print("You just earned 15 points.")       

age = 1
if age < 2:
    print("Person is a baby.")
elif age < 4:
    print("Person is a toddler.")
elif age < 13:
    print("Person is a kid.")
elif age < 20:
    print("Person is a teenager.")
elif age < 65:
    print("Person is an adult.")
else:
    print("Person is an elder.")

fruits = ['mango' , 'litchi' , 'apple' , 'grapes']
if 'mango' in fruits:
    print("mango")
if 'papaya' in fruits:
    print("papaya")
if 'litchi' in fruits:
    print("litchi")

favourite_fruits = ['litchi' , 'strawberry' , 'mango']
if 'litchi' in favourite_fruits:
    print("You really like litchi.")
if 'banana' in favourite_fruits:
    print("You really like bananas.")
if 'strawberry' in favourite_fruits:
    print("You really like strawberry.")
if 'apple' in favourite_fruits:
    print("You really like apple.")
if 'mango' in favourite_fruits:
    print("You really like mango.")

list = ['eric' , 'david' , 'admin' , 'carolina' , 'ady']
for list in list:
    if list == 'admin':
        print("Hello admin, Would you like to see status report?")
    else:
        print("Hello " + list + ", thank you for logging in again.")    

list = []
if list:
       for list in list:
           if list == 'admin':
               print("Hello admin, Would you like to see status report?")
           else:
               print("Hello " + list + ", thank you for logging in again.")
else:
    print("We need to find some users.")        

current_users = ['ram' , 'shyam' , 'sita' , 'geeta' , 'rita']
new_users = ['neetu' , 'ram' , 'ash' , 'sita' , 'reena']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great " + new_user + " is still available.")

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in number:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(str(num) + "th")


