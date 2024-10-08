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

def formatted_name(first_name , last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = formatted_name('eric' , 'maethes')
print(musician)

def formatted_name(first_name , middle_name , last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
musician = formatted_name('eric' , 'da' , 'maethes')
print(musician)

def formatted_name(first_name , last_name , middle_name = ''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = formatted_name('eric' , 'da' , 'maethes')
print(musician)
musician = formatted_name('eric' , 'maethes')
print(musician)

def build_person(first_name , last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('selena' , 'gomez')
print(musician)

def build_person(first_name , last_name , age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('selena' , 'gomez' , age = 30)
print(musician)

def formatted_name(first_name , last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' anytime to quit.)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    name = formatted_name(f_name , l_name)
    print("\nHello " + name.title() + "!")

def greet(names):
    """Print a greeting to each user in the list"""
    for name in names:
        msg = "Hello " + name.title() + "!"
        print(msg)
usernames = ['aelly' , 'eva' , 'sarah']
greet(usernames)

def print_model(unprinted_designs , completed_models):
    """Unprinted designs and completed models"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Show completed models"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iPhone case' , 'Samsung case' , 'robo pendant']
completed_models = []
print_model(unprinted_designs , completed_models)
show_completed_models(completed_models)

def make_pizza(*toppings):
    """Print the list of toppings."""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms' , 'extra cheese' , 'capsicum')

def make_pizza(*toppings):
    """Summarize the pizza we're about to make"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms' , 'extra cheese' , 'capsicum')

def make_pizza(size , *toppings):
    """Summarize the pizza we're about to make"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(12 , 'pepperoni')
make_pizza(15, 'mushrooms' , 'extra cheese' , 'capsicum')

def build_profile(first, last, **user_info):
    """Build a dictionary and store information about a user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
                             location = 'princeton',
                             field = 'physics')
print(user_profile)

