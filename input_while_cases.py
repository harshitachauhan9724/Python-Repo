# car = input("What kind of car would you like?")
# print("Let me find you a " + car + ".")

# restaurant = input("How many people are there in your dinner group?")
# restaurant = int(restaurant)
# if restaurant >= 8:
#    print("You will have to wait for a table.")
# else:
#    print("Your table is ready.")

# number = input("Enter a number.")
# number = int(number)
# if number % 10 == 0:
#    print(str(number) + " is a multiple of 10.")
# else:
#    print(str(number) + " is not a multiple of 10.")

# prompt = "\nEnter some pizza tooppings."
# prompt += "\nEnter 'quit' when you are finished."
# while True:
#     pizza = input(prompt)
#     if pizza == 'quit':
#         break
#     else:
#         print("Adding " + pizza.title() + ".")

# prompt = "\nHow old are you?"
# prompt += "\nEnter 'quit' when you are finished!"
# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)
#     if age < 3:
#         print("No charges!")
#     elif age <= 12:
#         print("The ticket price is $10.")
#     else:
#         print("The ticket price is $15.")

sandwich_orders = ['tuna sandwich' , 'cheese sandwich' , 'mexican sandwich']
finished_sandwiches = []
while sandwich_orders:
    order = sandwich_orders.pop()
    print("I made your " + order.title())
    finished_sandwiches.append(order)
print("\nThe following sandwiches have been made:")
for finish in finished_sandwiches:
    print(finish.title())

sandwich_orders = ['tuna sandwich' , 'cheese sandwich' , 'tuna sandwich' , 'mexican sandwich' , 'tuna sandwich']
finished_sandwiches = []
print("Sorry! We have run out of Tuna sandwiches today.")
while 'tuna sandwich' in sandwich_orders:
    sandwich_orders.remove('tuna sandwich')
print("\n")
while sandwich_orders:
    order = sandwich_orders.pop()
    print("I made your " + order.title())
    finished_sandwiches.append(order)
print("\nThe following sandwiches have been made:")
for finish in finished_sandwiches:
    print(finish.title())

responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    place = input("If you could visit one place in the world, where would you go?")
    responses[name] = place
    repeat = input("Would you like to let another person respond? (Yes/No)")
    if repeat == 'No':
        polling_active = False
print("\n---Poll Results---")
for name, place in responses.items():
    print(name + " would like to visit " + place + ".")

    
