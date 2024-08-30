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