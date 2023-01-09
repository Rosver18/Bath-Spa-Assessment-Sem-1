print("Exercise 1: Pizza Toppings")
print("    ")
toppingprompt = "\nWhat topping would you like on your pizza?"
toppingprompt += "\nEnter 'quit' when you are finished: " #using += to make the user add pizza toppings until they type quit
 
while True: #the while loop makes the whole code work as we use the toppingprompt variable as the input 
    pizzatopping = input(toppingprompt)
    if pizzatopping != 'quit': #if the player says something that is not "quit" the it will say that a topping has been added
        print(f"  The {pizzatopping} has been added to your pizza.")
    else:
        break