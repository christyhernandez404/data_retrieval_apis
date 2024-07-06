import requests
import json


pokemon_names = ["pikachu", "bulbasaur", "charmander"]

def fetch_pokemon_data(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    if response.status_code == 200:
        poke_data = response.json()
        return poke_data
    else:
        return None
    

for pokemon in pokemon_names:
        data_of_pokemon = fetch_pokemon_data(pokemon)
        if data_of_pokemon:
            print(f"Name: {pokemon}")
            print(f"Ability_1:{data_of_pokemon["abilities"][0]["ability"]["name"]}")
            print(f"Ability_2:{data_of_pokemon["abilities"][1]["ability"]["name"]}")
            print(f"Weight:{data_of_pokemon["weight"]}")

    

def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon in pokemon_list:
         poke_data = fetch_pokemon_data(pokemon)
         total_weight = poke_data['weight'] + total_weight
         avg = total_weight/len(pokemon_list)
    return print(f"Avg Weight: {avg}")

calculate_average_weight(pokemon_names)

