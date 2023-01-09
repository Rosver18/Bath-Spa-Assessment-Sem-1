print("Exercise 2: Movie Tickets")
print("    ")
ageprompt = "How old are you? "
#using += to make the user type their age until they type 'done'
ageprompt += "\ntype 'done' if you are finished: "

#using this while loop, we do the same thing as the pozza topping one 
#as we use the variable above as a loop to ask the user on how old they are
while True:
    age = input(ageprompt)
    if age == 'done':
        break
    age = int(age)
#the if statements here are used to determine what will display on what the user inputs in the prompt
#and if the user inputs anything above 13 then the else statement will be executed
    if age < 3:
        print("  You are under the age of 3 so you get in free!")
    elif age < 13:
        print("  You are under the age of 13 so your ticket is $10!")
    else:
        print("  You are over the age of 13 so your ticket is $15!")