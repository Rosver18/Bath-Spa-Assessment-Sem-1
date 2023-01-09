print("Exercise 4: Stages of Life")
print("    ")
#we use the int and input string to make people enter their age
age = int(input("Input your age: "))
#the if statements below show the requirements of each age and if the user's input is accurate to one if statement, 
#then it will show one of the print statements below and if one is higher than 65 years old, then it will use the else statement
if age < 2:
    print("You are a baby!")
elif age < 4:
    print("You are a toddler!")
elif age < 13:
    print("You are a kid!")
elif age < 20:
    print("You are a teenager!")
elif age < 65:
    print("You are an adult!")
else:
    print("You are an elder!")