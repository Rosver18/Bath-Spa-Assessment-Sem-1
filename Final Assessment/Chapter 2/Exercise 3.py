print("Exercise 3: Stripping Names")
print("    ")
#assigning the variable and using the \t function to make the following codes work
name = "\tRosver Jedh\n"
#printing the normal verion of the text is done by simply using a print string without any modifications
print("Normal:")
print(name)
#lstrip removes any whitespaces in the left side which in this case it removed the \t string
print("\nlstrip():")
print(name.lstrip())
#rstrip removes any whitespaces in the right side which in this case it never changed it's place in the display
print("\nrstrip():")
print(name.rstrip())
#strip removes any whitespaces which in this case it removed the \t string
print("\nstrip():")
print(name.strip())