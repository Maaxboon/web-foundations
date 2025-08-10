"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
"""
cities = {
    'kigali' : {
        'country': 'rwanda',
        'population': 3000000,
        'fact': 'city of a thousand hills',
    },
    'nairobi': {
        'country' : 'kenya',
        'population' : 3500000,
        'fact': 'city under the sun',
    },
    'kampala': {
        'country':'uganda',
        'population': 2800000,
        'fact': 'pearl of Africa'
    },
}

for city, city_info in cities.items():
    # print("\nCity: " + city.title())
    print(f"{city.title()} city located in {city_info['country'].title()} with a population of {city_info['population']} is known as the {city_info['fact']}.")