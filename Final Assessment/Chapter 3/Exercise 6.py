print("Exercise 6: Shrinking Guest List")
print("    ")
#in this variable, we use lists to display the names 
guests = ['Denji', 'Dennis', 'Yoru','Melissa','Mopper']

#in this variable, we use the list and the title string to automatically capitalize the name
name = guests[0].title()
#using the print string and the f string, we display the invitation message
print(f"{name}, you are invited to join the party later this evening.")

name = guests[1].title()
print(f"{name}, you are invited to join the party later this evening.")

name = guests[2].title()
print(f"{name}, you are invited to join the party later this evening.")

name = guests[1].title()
#using the print string and the f string, we display the message that they can't make it to the party
print(f"\nSorry, {name} can't make it to the party.")

#using the del string we delete one of the names in the list
del(guests[1])
#we use the insert function to add a name in the guest list
guests.insert(1, 'Asa')

name = guests[0].title()
#using the print string and the f string, we display the invitation message
print(f"\n{name}, you are invited to join the party later this evening.")

name = guests[1].title()
print(f"{name}, you are invited to join the party later this evening.")

name = guests[2].title()
print(f"{name}, you are invited to join the party later this evening.")

#we use this to display that there can be only 2 people in dinner
print("\nSorry, we can only invite two people to dinner.")

#using the pop string we delete one of the names in the list
name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the party.")

#using the pop string we delete one of the names in the list
name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the party.")

#using the pop string we delete one of the names in the list
name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the party.")

name = guests[0].title()
#using the print string and the f string, we display the invitation message
print(f"{name}, please come to the party.")

name = guests[1].title()
print(f"{name}, please come to the party.")

#we use the del function to delete the rest of the guests
del(guests[0])
del(guests[0])

#we use this to finally show how many people are going in the party
print(guests)