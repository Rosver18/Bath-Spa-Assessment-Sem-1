print("Exercise 5: USB Shopper")
print("    ")
#the print string shows the question
print("A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.")
#using this variable we can calculate the amount USB sticks
USBstick = 50 // 6 
#using this variable we can calculate how much money she has after buying USB Sticks
MoneyChange = 50 % 6
#using the print and the f strings we can display the answer of the question above
print (f"The girl can buy {USBstick} USB sticks, although she has {MoneyChange} euros left ")