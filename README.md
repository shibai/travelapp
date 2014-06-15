travelapp
=========

With Django Rest Framework

How to setup and run this service:
For Mac OS and Linux
#1 get pip
reference: https://pip.pypa.io/en/latest/installing.html
#2 get Django
$ pip install Django==1.6.5
reference: https://www.djangoproject.com/download/
#3 get Django Rest
$ pip install djangorestframework
reference: http://www.django-rest-framework.org/
#4 get South
$ pip install South
reference: http://south.readthedocs.org/en/latest/installation.html

Under directory travelapp/ (it contains manage.py)
$ python manage.py runserver
Then go to browser: localhost:8000/travelapp/api/..........
travelapp/travelapp/urls.py has all available APIs
