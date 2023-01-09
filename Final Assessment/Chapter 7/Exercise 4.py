print("Exercise 4: Large Shirts")
print("    ")
#this immediately adds on what will display on the sentences
def make_shirt(size='large', message='I love Python!'):

#this will be the main stentence on what would be displayed on the code
    print(f"\nThe current plan is to make a {size} t-shirt.")
    print(f'It will have "{message}" written on it')

#this will display the sentences normally
make_shirt()
#this will replace one of the words in the sentence from large to medium
make_shirt(size='medium')
#this will replace both of the parameters to another message and size
make_shirt('small', 'Kick Back')