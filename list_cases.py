friends = ['Prayag' , 'Ishan' , 'Harshi' , 'Ashish' , 'Pranjal']
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])

message = "I have many friends but " + friends[0] + " is my best friend."
print(message)
message = "I have many friends but " + friends[1] + " is my best friend."
print(message)
message = "I have many friends but " + friends[2] + " is my best friend."
print(message)
message = "I have many friends but " + friends[3] + " is my best friend."
print(message)
message = "I have many friends but " + friends[4] + " is my best friend."
print(message)

transport = ['car' , 'bike' , 'scooty']
print("I would like to own a " + transport[0] + ".")
print("I would like to own a " + transport[1] + ".")
print("I would like to own a " + transport[2] + ".")

guest = ['aru' , 'avi' , 'sam']
print(guest[0].title() + ", You are invited to the dinner party.")
print(guest[1].title() + ", You are invited to the dinner party.")
print(guest[2].title() + ", You are invited to the dinner party.")

print(guest[2].title() + " can't come to the dinner.")
guest.remove('sam')
print(guest)
guest.append('ash')
print(guest)

print(guest[0].title() + ", Please come to the dinner party.")
print(guest[1].title() + ", Please come to the dinner party.")
print(guest[2].title() + ", Please come to the dinner party.")

print("Oh...I just found a bigger dinner table.")
guest.insert(0, 'harshi')
guest.insert(3, 'pranjal')
guest.append('praisha')
print(guest)
name = guest[0].title()
print(name + " ,Please come to the dinner party.")
name = guest[1].title()
print(name + " ,Please come to the dinner party.")
name = guest[2].title()
print(name + " ,Please come to the dinner party.")
name = guest[3].title()
print(name + " ,Please come to the dinner party.")
name = guest[4].title()
print(name + " ,Please come to the dinner party.")
name = guest[5].title()
print(name + " ,Please come to the dinner party.")

print("Sorry, the new dinner table won't be available on time and i can invite only two people.")
pops = guest.pop()
print("Sorry, " + pops.title() + " I can't invite you to the dinner party.")
pops = guest.pop()
print("Sorry, " + pops.title() + " I can't invite you to the dinner party.")
pops = guest.pop()
print("Sorry, " + pops.title() + " I can't invite you to the dinner party.")
pops = guest.pop()
print("Sorry, " + pops.title() + " I can't invite you to the dinner party.")
print(guest)
name = guest[0].title()
print(name + ", You are invited.")
name = guest[1].title()
print(name + ", You are invited.")
del guest[0]
del guest[0]
print(guest)

places = ['switzerland' , 'paris' , 'noida' , 'nainital' , 'delhi']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

count_places = len(places)
print("{} places i want to visit".format(count_places))

print(places[-1])

my_list = []
print(my_list)
