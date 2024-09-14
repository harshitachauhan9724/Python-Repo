def greet(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")
greet('Eric')

def pet(animal_type , pet_name):
    """Display information about pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
pet('dog' , 'coco')
pet('cat' , 'liza')

def pet(animal_type , pet_name):
    """Display information about pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
pet(animal_type='dog' , pet_name='cherry')

def pet(pet_name , animal_type='dog'):
    """Display information about pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
pet(pet_name= 'candy' , animal_type= 'cat')

