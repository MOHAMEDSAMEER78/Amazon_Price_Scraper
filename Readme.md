create virtual environment
    python3 -m venv projenv 

activate virtual environment
    cd ..
    source projenv/bin/activate
    cd web_scraping_project


install django
    pip install django

Create project
	django-admin startproject web_scraping_project

create an app
    python3 manage.py startapp web_scraping

Create and Apply Migrations
    python3 manage.py makemigrations
    python3 manage.py migrate

Run
	python3 manage.py runserver