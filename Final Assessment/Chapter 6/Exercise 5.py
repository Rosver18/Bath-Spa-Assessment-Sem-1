print("Exercise 5: No Pastrami")
print("    ")
#using the same method as the last exercise but this time we have 3 pastaramis in the order list
sandwich_orders = ['Meat', 'Pizza', 'Bacon', 'chicken', 'pastrami', 'pastrami','pastrami']
finished_sandwiches = []

#using a while loop to remove every pastarami in the list
print("I apologize, but we've run out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

#using a while loop to do the usual making the sandwhich
print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm making your {current_sandwich} sandwich right now.")
#using append string to add items to the finished_sandwhiches list
    finished_sandwiches.append(current_sandwich)

#final part of the code where it shows everything in the finished_sandwhiches list
print("\n")
for sandwich in finished_sandwiches:
    print(f"Sorry to keep you waiting, here's your {sandwich} sandwich.")