print("Exercise 5: Pets")
print("    ")
#using variable to make a empty list
pets = []
#using a dictionary to make the details of the pets 
pet = {
    'animal type': 'Dog',
    'name': 'Otso',
    'owner': 'Rosver',
    'weight': 54,
    'eats': 'Dog food',
}
pets.append(pet) #using the append string to add another item in the list

pet = {
    'animal type': 'chicken',
    'name': 'Chika',
    'owner': 'Rosver',
    'weight': 28,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'Dog',
    'name': 'Dennis',
    'owner': 'Mama',
    'weight': 57,
    'eats': 'Meat',
}
pets.append(pet)
#using for loop to display everything on each dictionary in the list and to add some extra details like 
#adding a sentence to organize the display of the list
for pet in pets:
    print(f"\nHere's the existing information about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")