'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    print(poke_info)

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # Clean the Pokemon name parameter
    pokemon_name = str(pokemon_name).strip().lower()

    # Build the URL for the specific Pokemon
    url = POKE_API_URL + pokemon_name

    # Send GET request to PokeAPI
    print(f'Fetching information for Pokemon: {pokemon_name}...', end='')
    resp = requests.get(url)

    # Check if request was successful
    if resp.status_code == requests.codes.ok:
        print('success')
        return resp.json()  # Return JSON response as dictionary
    else:
        print('failure')
        print(f'Response code: {resp.status_code} ({resp.reason})')
        return None

if __name__ == '__main__':
    main()
