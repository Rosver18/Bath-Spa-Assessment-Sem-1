print("Exercise 1: Alien Colors #1")
print("    ")
#using this variable we assign that the alien color is yellow
alien_color = 'yellow'
#we use a if statement to say that if the alien color is yellow then the player gets 5 points
if alien_color == 'yellow':
    print("You just shot down a yellow alien and earned 5 points!")
#now we use this statement to say that the color is red
alien_color = 'red'
#now we use the same if statement as earlier but it fails since the variable is not yellow
if alien_color == 'yellow':
    print("You just shot down a yellow alien and earned 5 points!")