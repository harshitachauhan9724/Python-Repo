# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = input("Please tell me your name: ")
# print("Hello " + name + "!")

# prompt = "If you tell us who you are, we can personalize the message you see."
# prompt += "\nWhat is you name?"
# name = input(prompt)
# print("\nHello " + name + "!")

# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 36:
#    print("\nYou are tall enough to ride!")
# else:
#    print("\nYou will be able to ride when you are a little older!")

# number = input("Enter a number, and i will tell you if it's even or odd!")
# number = int(number)
# if number % 2 == 0:
#   print("\nThe number " + str(number) + " is even.")
# else:
#    print("\nThe number " + str(number) + " is")

# current_num = 1
# while current_num <= 5:
#     print(current_num)
#     current_num += 1

# prompt = "\nTell me something, and I will repeat it back to you."
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#       print(message)

# prompt = "\nTell me something, and I will repeat it back to you."
# prompt += "\nEnter 'quit' to end the program."
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# prompt = "\nEnter the name of the city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to "+ city.title()+"!")

# current_num = 0
# while current_num < 10:
#     current_num += 1
#     if current_num % 2 == 0:
#         continue
#     print(current_num)

x = 1
while x <= 5:
    print(x)
    x +=1

unconfirmed = ['alice' , 'reah' , 'sam']
confirmed = []
while unconfirmed:
    current = unconfirmed.pop()
    print("Verifying user: " + current.title())
    confirmed.append(current)
print("\nThe following users have been confirmed:")
for confirm in confirmed:
    print(confirm.title())

pets = ['dog' , 'cat' , 'dog' , 'goldfish' , 'cat' , 'rabbit' , 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n---Poll Results---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")