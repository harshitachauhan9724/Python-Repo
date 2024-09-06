person = {'first name': 'Eric' , 'last name': 'Mandela' , 'age': 50 , 'city': 'New York'}
print(person)

numbers = {
    'ash': 4,
    'ady': 6,
    'eric': 1,
    'ellie': 7,
    'nova': 2,
}
print(numbers)

glossary = {
    'variable': 'varia',
    'string': 'stri',
    'constant': 'const',
    'python': 'py',
}
word = 'variable'
print("\n" + word.title() + ": " + glossary[word])
word = 'string'
print("\n" + word.title() + ": " + glossary[word])
word = 'constant'
print("\n" + word.title() + ": " + glossary[word])
word = 'python'
print("\n" + word.title() + ": " + glossary[word])

glossary = {
    'variable': 'varia',
    'string': 'stri',
    'constant': 'const',
    'python': 'py',
    'loop': 'for',
    'condition': 'if',
    'otherwise': 'else',
}
for key, value in glossary.items():
    print("\nTerm: " + key.title())
    print("Meaning: " + value.title())

river = {
    'nile': 'egypt',
    'ganga': 'india',
    'amazon': 'america',
}
for water, place in river.items():
    print("The " + water.title() + " runs through " + place.title() + ".")
for water in river.keys():
    print(water.title())
for place in river.values():
    print(place.title())

language = {
    'jen': 'python',
    'david': 'c++',
    'ash': 'java',
    'edward': 'c++',
    }
for name, lang in language.items():
    print(name.title() + ": " + lang.title())
people = ['jen', 'phil', 'ash', 'sarah']
for names in people:
    if names in language.keys():
        print("Thankyou " + names.title() + ", for taking the poll.")
    else:
        print("Please " + names.title() + ", take the poll.")

person_0 = {'name': 'eric', 'profession': 'writer', 'age': 50}
person_1 = {'name': 'elsa', 'profession': 'engineer', 'age': 28}
person_2 = {'name': 'ashley', 'profession': 'artist', 'age': 40}
person = [person_0, person_1, person_2]
for people in person:
    print(people)

bholi = {'type': 'cow', 'owner': 'ram'}
bruno = {'type': 'dog', 'owner': 'david'}
sona = {'type': 'deer', 'owner': 'shyam'}
pet = [bholi, bruno, sona]
for animal in pet:
    print(animal)

places = {'delhi': 'richa', 'bombay': 'kru', 'chennai': 'ruhi'}
print("The favourite places of people are:")
for name, place in places.items():
    print(name.title() + ":" + place.title())

number = {
    'dev': [2, 4],
    'ady': [6],
    'noa': [1, 8],
    'mani': [3, 7],
}
for name, fav_num in number.items():
    print("\n" + name.title() + "'s favourite numbers are:")
    for fav in fav_num:
        print(fav)

cities = {
    'kathmandu' : {
        'country': 'nepal',
        'population': 1003285,
        'fact': 'mountains',
    },
    'bengaluru' : {
        'country': 'india',
        'population': 14008000,
        'fact': 'advanced',
    },
    'mumbai' : {
        'country': 'india',
        'population': 21673000,
        'fact': 'most populated',
    },
}
for name, info in cities.items():
    print("\nName:" + name.title())
    population = info['population']
    fact = info['fact']
    print("\tPopulation:" + str(population))
    print("\tFact:" + fact)