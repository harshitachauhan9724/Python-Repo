pizza = ['cheese burst' , 'sweet corn' , 'farmhouse']
for pizzas in pizza:
    #print(pizzas)

    print("I like " + pizzas.title() + " pizza.")
print("\nI really love pizza!")    

animals = ['cow' , 'buffalo', 'ox']
for animal in animals:
   # print(animal)
    print(animal.title() + " is a pet animal.")
print("\nAny of these animals would make a great pet.")    

for numbers in range(1,21):
    print(numbers)

number = list(range(1,1000001))    
print(number)

print(min(number))
print(max(number))
print(sum(number))

num = list(range(1,21,2))
for value in num:
    print(value)

multiples = list(range(3,31,3))
for value in multiples:
    print(value)

cube = []
for value in range(1,11):
    cubes = value**3
    cube.append(cubes)
print(cube) 

cube = [value**3 for value in range(1,11)]
print(cube)

flower = ['rose' , 'lily' , 'tulip' , 'gypsy' , 'sunflower']
print("The first three flowers in the list are: ")
for flowers in flower[:3]:
   print(flowers)
print("\nThe middle three flowers are: ")
print(flower[1:4])
print("\nThe last three flowers are: ")
print(flower[2:])

my_pizza = ['cheese burst' , 'sweet corn' , 'farmhouse']
friend_pizza = my_pizza[:]
my_pizza.append('supreme veg')
friend_pizza.append('cheese pepper')
print("My favourite pizzas are: ")
for pizzas in my_pizza[:]:
    print(pizzas)
print("My friend's favourite pizzas are: ")    
for pizzas in friend_pizza[:]:
    print(pizzas)

buffet = ('idli' , 'dosa' , 'dal' , 'rice' , 'poha')
for food in buffet:
    print(food)
#buffet[0] = 'curry'    
buffet = ('idli' , 'dosa' , 'dal' , 'rice' , 'poha')
print("Initial menu: ")
for items in buffet:
    print(items)
buffet = ('idli' , 'dosa' , 'dal' , 'curry' , 'upma')
print("\nRevised menu: ")
for items in buffet:
    print(items)