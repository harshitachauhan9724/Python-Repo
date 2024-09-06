alien = {'color': 'green' , 'points': 5}
print(alien['color'])
print(alien['points'])

alien = {'color': 'green' , 'points': 5}
new_points = alien['points']
print("You just earned " + str(new_points) + " points.")

alien = {'color': 'green' , 'points': 5}
print(alien)
alien['x-coordinate'] = 0
alien['y-coordinate'] = 25
print(alien)

alien = {}
alien['color'] = 'green'
alien['points'] = 5
print(alien)

alien = {'color': 'green'}
print("The alien is " + alien['color'] + ".")
alien['color'] = 'yellow'
print("The alien is now " + alien['color'] + ".")

alien = {'x-position': 0, 'y-position': 25, 'speed': 'medium'}
# alien['speed'] = 'fast'
print("Original x-position: " + str(alien['x-position']))
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien['x-position'] = alien['x-position'] + x_increment
print("New x-position: " + str(alien['x-position']))

alien = {'color': 'green' , 'points': 5}
print(alien)
del alien['points']
print(alien)

language = {
    'jen': 'python',
    'david': 'c++',
    'ash': 'java',
    'edward': 'c',
    }
print("David's favourite language is " +
       language['david'].title() + 
        ".")

user = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user.items():
    print("\nKey: " + key)
    print("Value: " + value)

language = {
    'jen': 'python',
    'david': 'c++',
    'ash': 'java',
    'edward': 'c',
    }
for name, languages in language.items():
    print(name.title() + "'s favourite language is " + languages.title() + ".")

for name in language.keys():
    print(name.title())

language = {
    'jen': 'python',
    'david': 'c++',
    'ash': 'java',
    'edward': 'c',
    }
friends = ['jen', 'edward']
for name in language.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + language[name].title() + "!")

if 'erin' not in language.keys():
    print("Erin, Please take our poll.")

for name in sorted(language.keys()):
    print(name.title() + ", Thankyou for taking our poll.")

print("The following languages have been mentioned:")
for name in language.values():
    print(name.title())

language = {
    'jen': 'python',
    'david': 'c++',
    'ash': 'java',
    'edward': 'c++',
    }
print("The following languages have been mentioned:")
for name in set(language.values()):
    print(name.title())

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

aliens = []
for alien_num in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print("You ordered a " + pizza['crust'] + "-crust pizza with the following pizza toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

languages = {
    'edward': ['c', 'python'],
    'ash': ['c'],
    'eric': ['c++', 'java'],
    'david': ['python', 'php'],
}
for name, language in languages.items():
    print("\n" + name.title() + "'s favourite languages are:")
    for lang in language:
        print("\t" + lang.title())

users = {
    'aeinstein' : {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie' : {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}
for username, info in users.items():
    print("\nUsername: " + username)
    full_name = info['first'] + " " + info['last']
    location = info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

