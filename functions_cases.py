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