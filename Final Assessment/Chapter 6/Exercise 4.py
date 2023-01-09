print("Exercise 4: Deli")
print("    ")
#making 2 variables one of them has a empty list as the finished sandwhich will be put there
sandwich_orders = ['Meat', 'Pizza', 'Bacon', 'chicken']
finished_sandwiches = []

#using this while loop we can make the ongoingsandwhich variable use the pop string to display what toppings are on the 
#sandwhich_orders variable
while sandwich_orders:
    ongoingsandwich = sandwich_orders.pop()
    print(f"I'm making your {ongoingsandwich} sandwich right now.")
#using the append string we can add the toppings in the finished_sandwhiches list  
    finished_sandwiches.append(ongoingsandwich)

#this is the final loop of the code as it displays everything in the finished_sandwhiches list
print("\n")
for sandwich in finished_sandwiches:
    print(f"Sorry to keep you waiting, here's your {sandwich} sandwich.")