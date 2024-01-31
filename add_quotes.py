# bulk_add_quotes.py

# A script to add quotes from futurama_quotes.txt in bulk
import os
import requests

# Basic User Authentication
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
# Dev URL
DOMAIN = 'http://127.0.0.1:8000'



def get_character_url(_character):
    # First we get all characters
    url = f"{DOMAIN}/api/characters/"
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers, auth=(USERNAME, PASSWORD))
    chars = response.json()
    char_url = None
    for character in chars['results']:
        if character['name'].lower() == _character.lower():
            char_url = character['url']
    print(char_url)
    return char_url


def post_character(_character):
    url = f"{DOMAIN}/api/characters/"
    payload = {
        "name": _character
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers, auth=(USERNAME, PASSWORD))
    # print(response.status_code)
    if response.status_code == 201:
        print(response.json())
        return True
    else:
        print('Something went wrong, doh!')
        return False


def post_quote(_quote, _character_url):
    url = f"{DOMAIN}/api/quotes/"
    payload = {
        "quote_text": _quote,
        "character": _character_url
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers, auth=(USERNAME, PASSWORD))
    print(response.status_code)
    if response.status_code == 201:
        print(response.json())
        return True
    else:
        print('Something went wrong, doh!')
        return False


def main():
    # Open our pre-populated quote file
    quote_file = open('futurama_quotes.txt', 'r+')
    # Read all the lines
    lines = quote_file.readlines()
    # Iterate over the lines
    for data in lines:
        # Split the line on the colon
        character, quote = data.split(': ')
        # Find our character
        try:
            # Get the character URL
            char_url = get_character_url(_character=character)
            if char_url is None:
                # Add the character if missing
                added_character = post_character(_character=character)
                if added_character:
                    print(f"New Character Added: {character}")
                    char_url = added_character['url']
                else:
                    print(f"DOH! Something failed adding: {character}")
                    char_url = ''

            # Add the quote, and assign to the character
            added = post_quote(_quote=quote, _character_url=char_url)
            if added:
                print(f"Added: {quote}")
            else:
                print('Something went wrong, doh!')
        except:
            # We broke something
            print('Frack!')


if __name__ == '__main__':
    # TODO setup a dev vs prod conditional
    main()
