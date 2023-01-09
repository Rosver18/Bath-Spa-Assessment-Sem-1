print("Exercise 2: Glossary")
print("    ")
#using the dictionary function to put the glossary details
glossary = {
    'string': 'Strings are used for storing characters.',
    'comment': 'Commenting involves placing Human Readable Descriptions inside of computer programs detailing what the Code is doing.',
    'list': 'List is the most versatile data type available in functional programming languages used to store a collection of similar data items.',
    'loop': 'a loop is a sequence of instruction s that is continually repeated until a certain condition is reached.',
    'Arrays': 'Arrays are used to group together similar variables.',
    }
#using the variable to show the contents of the glossary and using the title strings to modify the texts
word1 = 'string'
print(f"\n{word1.title()}: {glossary[word1]}")

word2 = 'comment'
print(f"\n{word2.title()}: {glossary[word2]}")

word3 = 'list'
print(f"\n{word3.title()}: {glossary[word3]}")

word4 = 'loop'
print(f"\n{word4.title()}: {glossary[word4]}")

word5 = 'Arrays'
print(f"\n{word5.title()}: {glossary[word5]}")