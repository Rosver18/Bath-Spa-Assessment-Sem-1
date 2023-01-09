print("Exercise 3: T-Shirt")
print("    ")
#using def and 2 parameters to set up on what would be put in a shirt and what size it would be
def make_shirt(size, message):

#this will display on what the shirt will be 
    print(f"\nThe current plan is to make a {size} t-shirt.")
    print(f'It will have "{message}" written on it')

#this will determine what would be put in size and message
make_shirt('large', 'Kick Back')
#this will do basically the same thing
make_shirt(message="In The Backrooms", size='medium')