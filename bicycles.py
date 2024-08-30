bicycles = ['trek' , 'avon' , 'hero' , 'ladybird']
print(bicycles)
print(bicycles[0])
print(bicycles[1].title())
print(bicycles[-1])
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

motorcycles = ['honda' , 'hero' , 'yamaha']
print(motorcycles)

motorcycles[1] = 'suzuki'
print(motorcycles)

motorcycles.append('hero')
print(motorcycles)

bikes = []
bikes.append('honda')
bikes.append('hero')
bikes.append('suzuki')
print(bikes)

bikes.insert(0, 'yamaha')
print(bikes)

del bikes[0]
print(bikes)
del bikes[1]
print(bikes)

cycle = ['hero' , 'honda' , 'avon' , 'suzuki']
print(cycle)
popped_cycle = cycle.pop()
print(cycle)
print(popped_cycle)

last_owned = cycle.pop()
print("The last cycle i owned was a " + last_owned.title() + ".")

first_owned = cycle.pop(0)
print("The first cycle i owned was a " + first_owned.title() + ".")

cycles = ['suzuki' , 'hero' , 'honda' , 'bugati']
print(cycles)
#cycles.remove('bugati')
#print(cycles)

too_expensive = 'bugati'
cycles.remove(too_expensive)
print(cycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

cars = ['bmw' , 'audi' , 'toyota' , 'mahindra']
#cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

print("Here is the original list: ")
print(cars)
print("Here is the sorted list: ")
print(sorted(cars))
print("Here is the original list again: ")
print(cars)

cars.reverse()
print(cars)






