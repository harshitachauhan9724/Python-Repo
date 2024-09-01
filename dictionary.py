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

