print("Exercise 3: Glossary 2")
print("    ")
#using the dictionary function to put the glossary details
glossary = {
    'string': 'Strings are used for storing characters.',
    'comment': 'Commenting involves placing Human Readable Descriptions inside of computer programs detailing what the Code is doing.',
    'list': 'List is the most versatile data type available in functional programming languages used to store a collection of similar data items.',
    'loop': 'a loop is a sequence of instruction s that is continually repeated until a certain condition is reached.',
    'Arrays': 'Arrays are used to group together similar variables.',
    'float': 'A numerical value with a decimal component.',
    'Arithmetic operators': 'Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication and division.',
    }
#using a for loop and the item string to display everyting in the glossary with the word and it's definition 
for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")