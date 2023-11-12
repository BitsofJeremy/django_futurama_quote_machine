# bulk_add_quotes.py

# A script to add quotes from futurama_quotes.txt in bulk
import os
import requests

# Add user key
API_KEY = os.getenv('API_KEY')
# Dev
DOMAIN = 'http://127.0.0.1:8000'
# Prod
# DOMAIN = 'https://fqm.deafmice.com'


def get_character_url(_character):
    # First we get all characters
    # TODO make idiot safe with try/except
    url = f"{DOMAIN}/api/characters/"
    headers = {"Authorization": f"Basic {API_KEY}"}
    response = requests.get(url, headers=headers)
    chars = response.json()
    char_url = None
    for character in chars['results']:
        if character['name'].lower() == _character.lower():
            char_url = character['url']
    return char_url


def post_quote(_quote, _character_url):
    # TODO make idiot safe with try/except
    # TODO Add a query for previously added quotes
    url = f"{DOMAIN}/api/quotes/"
    payload = {
        "quote_text": _quote,
        "character": _character_url
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {API_KEY}"
    }
    response = requests.post(url, json=payload, headers=headers)
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
            char_url = get_character_url(character)
            # Add the quote, and assign the character
            added = post_quote(quote, char_url)
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
