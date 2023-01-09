print("Exercise 5: Change Guest List")
print("    ")
#in this variable, we use lists to display the names 
guests = ['Denji', 'Dennis', 'Yoru']

#in this variable, we use the list and the title string to automatically capitalize the name
name = guests[0].title()
#using the print string and the f string, we display the invitation message
print(f"{name}, you are invited to join the party later this evening.")

name = guests[1].title()
print(f"{name}, you are invited to join the party later this evening.")

name = guests[2].title()
print(f"{name}, you are invited to join the party later this evening.")

#using the print string and the f string, we display the message that they can't make it to the party
name = guests[1].title()
print(f"\nSorry, {name} can't make it to the party.")

#we use the del string to delete one of the guests
del(guests[1])
#we use the insert string to put a replacement to the deleted name
guests.insert(1, 'Asa')

#in this variable, we use the list and the title string to automatically capitalize the name
name = guests[0].title()
#using the print string and the f string, we display the invitation message
print(f"\n{name}, you are invited to join the party later this evening.")

name = guests[1].title()
print(f"{name}, you are invited to join the party later this evening.")

name = guests[2].title()
print(f"{name}, you are invited to join the party later this evening.")