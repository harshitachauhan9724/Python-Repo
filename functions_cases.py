def display_message():
    """Learning in this chapter."""
    print("We're learning functions.")
display_message()

def favourite_book(title):
    """Favourite book."""
    print("One of my favourite books is " + title.title() + ".")
favourite_book('alice in wonderland')

def make_shirt(size , text):
    """Information about shirt."""
    print("\nThe size of the shirt is " + size + ".")
    print("The text on the shirt should be " + text.title() + ".")
make_shirt('small' , 'apna din aayega')
make_shirt(size= 'small' , text= 'apna din aayega')

def make_shirt(text , size = 'large'):
    """Information about shirt."""
    print("\nThe size of the shirt is " + size + ".")
    print("The text on the shirt should be " + text.title() + ".")
make_shirt('i love python')
make_shirt(text= 'i love python' , size= 'medium')
make_shirt('i love ice-cream' , 'x-large')

def describe_city(name , country = 'india'):
    """Information about city."""
    print("\n" + name.title() + " is in " + country.title() + ".")
describe_city('bangalore')
describe_city('gurugram')
describe_city('bastille' , 'paris')

def city_country(name , country):
    """Return a city name and it's country."""
    country_city =  name + ", " + country
    return country_city.title()
cities = city_country('bangalore' , 'india')
print(cities)
cities = city_country('noida' , 'india')
print(cities)
cities = city_country('karachi' , 'pakistan')
print(cities)

def make_album(name , title , tracks=''):
    """Builds a dictionary with artist's name and title."""
    album = {'names':name , 'titles':title}
    if tracks:
        album['tracks'] = tracks
    return album
artist = make_album('ruskin bond' , 'beehive')
print(artist)
artist = make_album('harry potter' , 'harry potter series')
print(artist)
artist = make_album('premchand' , 'bal bharti')
print(artist)
artist = make_album('love' , 'henry' , tracks=3)
print(artist)

def make_album(name , title):
    """Builds a dictionary with artist's name and title."""
    album = {'names':name , 'titles':title}
    return album
while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' anytime to quit)")
    artist_name = input("Name:")
    if artist_name == 'q':
        break
    artist_title = input("Title:")
    if artist_title == 'q':
        break
    artist_album = make_album(artist_name , artist_title)
    print(artist_album)

def show_magicians(name):
    """Display the name of magicians"""
    for names in name:
        magician = names.title()
        print(magician)
magicians = ['charlie' , 'harry' , 'eric']
show_magicians(magicians)

def show_magicians(names , great_names):
    """Name of magicians"""
    while names:
        current = names.pop()
        print(current.title())
        great_names.append(current)
def make_great(great_names):
    """Add great"""
    for great in great_names:
        print(great.title() + ' the Great')
names = ['charlie' , 'harry' , 'eric']
great_names = []
show_magicians(names , great_names)
make_great(great_names)

def sandwich(*toppings):
    """Making a sandwich"""
    print("\nMaking a sandwich with items:")
    for items in toppings:
        print("- " + items)
sandwich('cheese')
sandwich('capsicum' , 'cheese')
sandwich('tomato' , 'capsicum' , 'cheese')

def profile(first, last, **info):
    """My info"""
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in info.items():
        profile[key] = value
    return profile
user = profile('harshi', 'rajput',
               location = 'india',
               hobbies = 'singing')
print(user)

def car(name, model, **info):
    """Car info"""
    cars = {}
    cars['names'] = name
    cars['models'] = model
    for key, value in info.items():
        cars[key] = value
    return cars
call = car('Tata', 'Nexon',
           color = 'red',
           price = '14 lac')
print(call)

