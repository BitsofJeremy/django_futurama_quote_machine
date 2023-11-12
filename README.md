# Django Futurama Quote Machine

A Django App that returns Futurama quotes

Online here:  https://fqm.funinternetthings.com

![](Screenshot3.png)

### Get it

Clone the repo

    git clone https://gitlab.com/abvavgjeremy/django_futurama_quote_machine.git

Setup you virtualenv and activate it

    virtualenv -p python3 venv
    source venv/bin/activate

Install requirements

    pip install -r requirements.txt

Create you SQLite DB

    python manage.py migrate

Create an admin

    python manage.py createsuperuser

Run the server

  python manage.py runserver

Open http://127.0.0.1:8000

Enjoy a nice quote!

#### App Screenshot

![Screenshot1](Screenshot1.png)

### Setup DB and inset quotes

- TODO Write this 'how to'

    

### API

Basic routes setup in the API

http://127.0.0.1:8000/api


#### API Screenshot

![Screenshot2](Screenshot2.png)
