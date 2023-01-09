Itemlist = [] #Empty Item List for the list below

Items = {'item code': '121', 'price': 5.25, 'Item': 'Snickers',} #set of dictionaries to put the item code, price, and the item
Itemlist.append(Items) #this will add the dictionary to the item list variable above

Items = {'item code': '122', 'price': 1.50, 'Item': 'Reeses',}
Itemlist.append(Items)

Items = {'item code': '123', 'price': 2.25, 'Item': 'Coca Cola',}
Itemlist.append(Items)

Items = {'item code': '124', 'price': 3.25, 'Item': 'Extra Bubblegum',}
Itemlist.append(Items)

Items = {'item code': '125', 'price': 4.50, 'Item': 'Doritos Chips',}
Itemlist.append(Items)

Items = {'item code': '126', 'price': 5.00, 'Item': 'Cup Noodles',}
Itemlist.append(Items)

Items = {'item code': '127', 'price': 0.50, 'Item': 'M&Ms',}
Itemlist.append(Items)

Items = {'item code': '128', 'price': 2.50, 'Item': 'Galaxy Chocolate',}
Itemlist.append(Items)

Items = {'item code': '129', 'price': 3.00, 'Item': 'Maltesers',}
Itemlist.append(Items)

Items = {'item code': '130', 'price': 4.50, 'Item': 'Mountain Dew',}
Itemlist.append(Items)


print("          ____________") #Vending machine art display
print("         ||┌───────┐ |")
print("         |│![] [] [] │")
print("         ||:l三三三! |")
print("         |│![] [] [] │")
print("         ||:l三三三! |")
print("         |│![] [] [] │")
print("         ||:l三三三! |")
print("         |│!     []  │")
print("         ||  ┌────┐ ||")
print("Hello! Welcome to the Vending Machine!")

for i in Itemlist:
      print(f"\nItem: {i['Item']} | Price: {i['price']} | Item Code: {i['item code']}") #for loop for displaying the list above

SnickersPrice = 5.25 #variables for the item prices
Reeses = 1.50
Coca_Cola = 2.25
Extra = 3.25
Doritos_Chips = 4.50
Cup_Noodles = 5.00
MandMs = 0.50
Galaxy = 2.50
Maltesers = 3.00
MtnDew = 4.50

MachineCash = 0 #empty variable for the cash

MachineCash = float(input("\nEnter the amount of money you will spend: ")) #to input the cash that the player will use
if MachineCash < 0.5:
    exit() #if player's money is less than 0.5 dollars then the code will end 

Item_selection = input("Select the item that you will buy: ") #this will make the person input the item code


if Item_selection == '121': #entering this code will show that they have chosen the desired item that they want
    print("You have chosen to buy a Snickers, that will cost 5.25 dollars") 
    if MachineCash < SnickersPrice: #this will only appear if the player's money is less than the price of the item, this will immediately end the app
        print("Sorry, you don't have enough cash for the product")
        exit()
    elif MachineCash >= SnickersPrice: #this will appear when the user has enough money for the item and it will show that the item has been dispensed
        MachineCash -= SnickersPrice
        print('cash returned: ' + str(MachineCash) + "\nYour Snickers has been dispensed, have a nice day!")

elif Item_selection == '122': #entering this code will show that they have chosen the desired item that they want
    print("You have chosen to buy a Reeses, that will cost 1.50 dollars")
    if MachineCash < Reeses: #this will only appear if the player's money is less than the price of the item, this will immediately end the app
        print("Sorry, you don't have enough cash for the product")
        exit()
    elif MachineCash >= Reeses: #this will appear when the user has enough money for the item and it will show that the item has been dispensed
        MachineCash -= Reeses
        print('Here is your Change: ' + str(MachineCash) + "\nYour Reeses has been dispensed, have a nice day!")

elif Item_selection == '123': #entering this code will show that they have chosen the desired item that they want
    print("You have chosen to buy a Coca Cola, that will cost 2.25 dollars")
    if MachineCash < Coca_Cola: #this will only appear if the player's money is less than the price of the item, this will immediately end the app
        print("Sorry, you don't have enough cash for the product")
        exit()
    elif MachineCash >= Coca_Cola: #this will appear when the user has enough money for the item and it will show that the item has been dispensed
        MachineCash -= Coca_Cola
        print('Here is your Change: ' + str(MachineCash) + "\nYour Coca Cola has been dispensed, have a nice day!")

elif Item_selection == '124': #entering this code will show that they have chosen the desired item that they want
    print("You have chosen to buy a Extra Bubblegum, that will cost 3.25 dollars")
    if MachineCash < Extra: #this will only appear if the player's money is less than the price of the item, this will immediately end the app
        print("Sorry, you don't have enough cash for the product")
        exit()
    elif MachineCash >= Extra: #this will appear when the user has enough money for the item and it will show that the item has been dispensed
        MachineCash -= Extra
        print('Here is your Change: ' + str(MachineCash) + "\nYour Extra Bubblegum has been dispensed, have a nice day!")

elif Item_selection == '125': #entering this code will show that they have chosen the desired item that they want
    print("You have chosen to buy a Doritos Chips, that will cost 4.50 dollars")
    if MachineCash < Doritos_Chips: #this will only appear if the player's money is less than the price of the item, this will immediately end the app
        print("Sorry, you don't have enough cash for the product")
        exit()
    elif MachineCash >= Doritos_Chips: #this will appear when the user has enough money for the item and it will show that the item has been dispensed
        MachineCash -= Doritos_Chips
        print('Here is your Change: ' + str(MachineCash) + "\nYour Doritos Chips has been dispensed, have a nice day!")

elif Item_selection == '126': #entering this code will show that they have chosen the desired item that they want
    print("You have chosen to buy a Cup Noodles, that will cost 5.00 dollars")
    if MachineCash < Cup_Noodles: #this will only appear if the player's money is less than the price of the item, this will immediately end the app
        print("Sorry, you don't have enough cash for the product")
        exit()
    elif MachineCash >= Cup_Noodles: #this will appear when the user has enough money for the item and it will show that the item has been dispensed
        MachineCash -= Cup_Noodles
        print('Here is your Change: ' + str(MachineCash) + "\nYour Cup Noodles has been dispensed, have a nice day!")

elif Item_selection == '127': #entering this code will show that they have chosen the desired item that they want
    print("You have chosen to buy a M&MS, that will cost 0.50 dollars")
    if MachineCash < MandMs: #this will only appear if the player's money is less than the price of the item, this will immediately end the app
        print("Sorry, you don't have enough cash for the product")
        exit()
    elif MachineCash >= MandMs: #this will appear when the user has enough money for the item and it will show that the item has been dispensed
        MachineCash -= MandMs
        print('Here is your Change: ' + str(MachineCash) + "\nYour M&Ms has been dispensed, have a nice day!")

elif Item_selection == '128': #entering this code will show that they have chosen the desired item that they want
    print("You have chosen to buy a Galaxy Chocolate, that will cost 2.50 dollars")
    if MachineCash < Galaxy: #this will only appear if the player's money is less than the price of the item, this will immediately end the app
        print("Sorry, you don't have enough cash for the product")
        exit()
    elif MachineCash >= Galaxy: #this will appear when the user has enough money for the item and it will show that the item has been dispensed
        MachineCash -= Galaxy
        print('Here is your Change: ' + str(MachineCash) + "\nYour Galaxy Chocolate has been dispensed, have a nice day!")

elif Item_selection == '129': #entering this code will show that they have chosen the desired item that they want
    print("You have chosen to buy a Maltesers, that will cost 3.00 dollars")
    if MachineCash < Maltesers: #this will only appear if the player's money is less than the price of the item, this will immediately end the app
        print("Sorry, you don't have enough cash for the product")
        exit()
    elif MachineCash >= Maltesers: #this will appear when the user has enough money for the item and it will show that the item has been dispensed
        MachineCash -= Maltesers
        print('Here is your Change: ' + str(MachineCash) + "\nYour Maltesers has been dispensed, have a nice day!")

elif Item_selection == '130': #entering this code will show that they have chosen the desired item that they want
    print("You have chosen to buy a Mountain Dew, that will cost 4.50 dollars")
    if MachineCash < MtnDew: #this will only appear if the player's money is less than the price of the item, this will immediately end the app
        print("Sorry, you don't have enough cash for the product")
        exit()
    elif MachineCash >= MtnDew: #this will appear when the user has enough money for the item and it will show that the item has been dispensed
        MachineCash -= MtnDew
        print('Here is your Change: ' + str(MachineCash) + "\nYour Mountain Dew has been dispensed, have a nice day!")
else: #this will display that there was an error in the input
    print("Error")
    