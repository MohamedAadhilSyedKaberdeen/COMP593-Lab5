""" 
Description: 
  Creates a new PasteBin paste that contains a list of abilities 
  for a specified Pokemon

Usage:
  python pokemon_paste.py poke_name

Parameters:
  poke_name = Pokemon name
"""
import sys
import poke_api
import pastebin_api

def main():
    poke_name = get_pokemon_name()
    if poke_name:
        poke_info = poke_api.get_pokemon_info(poke_name)
        if poke_info:
            paste_title, paste_body = get_paste_data(poke_info)
            paste_url = pastebin_api.post_new_paste(paste_title, paste_body, '1M')
            if paste_url:
                print(f'Paste created successfully: {paste_url}')
            else:
                print('Failed to create paste.')
        else:
            print(f'Failed to get Pokemon information for {poke_name}.')
    else:
        print('Pokemon name not provided.')

def get_pokemon_name():
    """Gets the name of the Pokemon specified as a command line parameter.
    Aborts script execution if no command line parameter was provided.

    Returns:
        str: Pokemon name
    """
    if len(sys.argv) >= 2:
        return sys.argv[1]
    else:
        return None

def get_paste_data(pokemon_info):
    """Builds the title and body text for a PasteBin paste that lists a Pokemon's abilities.

    Args:
        pokemon_info (dict): Dictionary of Pokemon information

    Returns:
        (str, str): Title and body text for the PasteBin paste
    """    
    # Build the paste title
    pokemon_name = pokemon_info.get('name', 'Unknown Pokemon').capitalize()
    title = f"{pokemon_name}'s Abilities"

    # Build the paste body text
    abilities = pokemon_info.get('abilities', [])
    body_text = '\n'.join([f'- {ability["ability"]["name"]}' for ability in abilities])

    return title, body_text

if __name__ == '__main__':
    main()
