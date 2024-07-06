import requests
import json

def pikachu():
    response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
    if response.status_code == 200:
        poke_data = response.json()

        poke_dict = {
            "name":poke_data["name"],
            "ability_1":poke_data["abilities"][0]["ability"]["name"],
            "ability_2":poke_data["abilities"][1]["ability"]["name"]

        }

        print(poke_dict)

pikachu()

