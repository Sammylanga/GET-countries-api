# GET-countries-api

Apply migrations to create the database tables:
    python manage.py makemigrations
    python manage.py migrate

Run the development server
    python manage.py runserver

Endpoint for all countries:
   https://restcountries.com/v3/all

Activate Virtual Environment
    source venv/bin/activate   

Add new countries to a new database
    python manage.py update_countries
