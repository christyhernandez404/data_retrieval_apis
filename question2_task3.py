import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    planet_data = {}

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet['name']
            mass = planet['mass']['massValue']
            planet_data[name] = mass
    return planet_data

def find_heaviest_planet(planet_dict):
    heavist_planet = None
    largest_mass = 0
    for name, mass in planet_dict.items():
        if mass > largest_mass:
            largest_mass = mass
            heavist_planet = name
    return heavist_planet, largest_mass

planet_dict = fetch_planet_data()
name, mass = find_heaviest_planet(planet_dict)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")