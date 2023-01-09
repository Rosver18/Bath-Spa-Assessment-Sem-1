print("Exercise 5: Cities")
print("    ")
#this alr establishes on what the country would be displayed
def describe_city(city, country='Philippines'):
#this is the main code that will be displayer    
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

#this will add manila to the city parameter
describe_city('Manila')
#this will replace the philippines display and add new york as the city
describe_city('New York', 'America')
#this will only add davao as the city parameter
describe_city('Davao')