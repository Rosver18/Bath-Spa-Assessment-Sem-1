print("Exercise 2: Alien Colors #2")
print("    ")
#using this variable we assign that the alien color is green
alien_color = 'green'
#we use a if statement to say that if the alien color is green then the player gets 5 points
if alien_color == 'green':
    print("You just shot down a green alien and earned 5 points!")
#we use the else statement to state that if the variable has another color it would display that the player gets 10 points 
else:
    print("You just shot down a alien and earned 10 points!")
#we used the same variable but now the color is red
alien_color = 'red'
#now it will show  the else statement since the variable is not 'green'
if alien_color == 'green':
    print("You just shot down a green alien and earned 5 points!")
else:
    print("You just shot down a alien and earned 10 points!")