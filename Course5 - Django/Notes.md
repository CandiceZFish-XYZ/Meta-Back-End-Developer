# Course 5 - Django

## Course Summary

1. Organize code in the DRY principle
2. use MVT framework to ensure reusability
3. Create a project and apps with correct structure
4. basic commands: django-admin, manage.py

View

1. Create views and view logic to process HTTP requests
2. Map URLs to views
3. use of request and response objects for common operations
4. Regex in URL patterns
5. Parameters in HTTP methods: GET, PUT, POST, DELETE

Model

1. Create Models
2. Apply migrations using best practice approach ??
3. use QuerySet API to interact with the database
4. Create form and use Form API to bind data to objects
5. Admin panel to control permissions of users and groups
6. setup MySQL db

Template

1. Use django templating language (DTL) to generate HTML markup for dynamic content
2. implement template inheritance

## Congifurations

### General setup

Install python3 on local machine.

#### Setup virtual environment

Option 1 - pip

- install pip `python3 -m pip install --user --upgrade pip`
- install venv `python3 -m pip install --user virtualenv`
- create virtual environment `python3 -m venv env_folder_name` at the location for project directories
- activate to work in the virtual env `source env_folder_name/bin/activate`, denoted by `(env_folder_name) path...`
- `deactivate`

Option 2 - pipenv

#### Start a Django project and app

Navigate to virtual env folder, install django.

- check `python3 -m django --version`
- or install `pip3 install django`

- startproject in the virtual env `django-admin startproject <projectname> `

  - for a/(the inner) folder to be recognized as a Python package must contain a file `__init__.py`

- startapp `python3 manage.py startapp <appname>` (inside the outer project folder)

#### migrations

- makemigrations `python3 manage.py makemigrations` to generate db table whose structure matches the data model declared in teh app using the ORM technique
- migrate `python3 manage.py migrate` to synchronize with database
- `showmigrations`

#### Shell

- `python3 manage.py shell` opens up an interactive Python shell inside the project to perform some quick interactive operations.

#### runserver

- `python3 manage.py runserver`

### project level

#### `settings.py`

- add new apps in the `INSTALLED_APPS` list
- DEBUG = True
- ALLOWED HOSTS
  - Add `0.0.0.0:8000` to make the site running on localhost externally visible,

#### `urls.py`

- Map view funtions in app `urls.py`, then `include` in the project `urls.py`.
  - e.g. in app url: `path('myapp/', views.index, name='index'),` and in project `path('myapp/', include('myapp.urls')),`
  - we can go to both to have the same view! `localhost:8000/myapp` & `localhost:8000/myapp/myapp/`

#### Database

- default SQLite on PORT 8000, can change to MySQL on PORT 3306
- `python3 manage.py createsuperuser`
  MySQL settings :

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangotest',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### App level

#### View

#### Model

- register in the app's `admin.py` then migrates
- To display data entry with semantic string names in django admin page, add function to the data model `def __str__(self) -> str: return self.first_name`

#### Form

1. Define data models in `models.py` and register in `admin.py`
2. create `forms.py` with code below
3. map url and create the view function to handle POST request,
4. render with a html themplate

```py
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
```

#### Database & users

- (login as admin) add entry, add user, assign permissions

## NOTES

### Django Architecture

Principles

- DRY
- Implementation of MVT architecture

Application structure

- Project
- App

Administration task

- django-admin
- manage.py

Web frameworks

- clean, ordered structure
- Fast, feature-rich classes, security, scalability

### Model of MVT

- Concept of Migrations & best approach to apply
- use QuerySet to interact with database
- create Form and use Form API to bind data to objects, and building model forms, html forms
- explored Admin panel to setup permission of users and groups
- setup external mysql database

### View of MVT

- create view and view logic to process(handles request and returns response) basic HTTP requests
- create view functions (in python) and different ways of mapping to the urlpatterns for Routing
  - process and retrieve data from db
  - transform data ???
  - render templates
- `urls.py` configuration
- HTTP request and map to urls and common CRUD operations
- get info by calling the client ???
- URL parameters
- Query parameters
- Handle errors with HTTP status responses
- simplify views by using OOP techniques: inheritance and reusability

### Template of MVT

- DTL, dynamic contents and map objects to the template
- template inheritance: split content into individual components and reuse the segments
  - the include tag: `{% include 'partials/_header.html' %}`
  - extends: `{% extends 'base.html' %}`
- Debug: `debugger = True`
- Testing for quality, reliability and performance
  - Unit testing
  - class based approach: inherits `from django.test import TestCase`

### Databases - MySQL

- Set up MySQL on local machine
  - `mysql -u root -p`
- Install MySQl DB API Driver
  - install `mysqlclient` to map python query to the model
  - connection time: `CONN_MAX_AGE`
- Update MySQL settings inside Django
- Set up database tables

### Test
