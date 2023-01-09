print("Exercise 4: Rivers")
print("    ")
#using the dictionary to put multiple countries and it's rivers
rivers = {
    'Pasig': 'Philippines',
    'Mississippi': 'united states',
    'Shinano': 'Japan',
    }
#using for loop to make 3 sentences with the items string
for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

#the keys function is used to display only the rivers in order from top to bottom
print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")
    
#the values() string is used to only show the countries in the dictionary
print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")