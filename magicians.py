magicians = ['david' , 'ady' , 'carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick " + magician.title() + ".\n")

print("Thank you everyone, that was a great magic show!")    

message = 'Hello python world!'
print(message)

for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

number = list(range(2,11,2))
print(number)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)    

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

square = [value**2 for value in range(1,11)]
print(square)

players = ['ronaldo' , 'kohli' , 'hardik' , 'rohit' , 'yuvraj']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())

my_foods = ['cake' , 'kulfi' , 'pav bhaji']    
friend_foods = my_foods[:]
my_foods.append('ice cream')
friend_foods.append('momos')
print("My favourite foods are: ")
print(my_foods)
print("\nMy friend's favourite foods are: ")
print(friend_foods)

dimension = (200 , 50)
print(dimension[0])
print(dimension[1])

#dimension[0] = 250

for dimensions in dimension:
    print(dimensions)

dimensions = (200, 50)
print("Original dimensions are: ")    
for dim in dimensions:
    print(dim)
dimensions = (400, 100)
print("\nModified dimensions: ")
for dim in dimensions:
    print(dim)