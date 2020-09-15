# Inovola-task

### Description

A client is building an e-commerce mobile application for their line of coffee machines and custom coffee pods; they are
looking to have two screens: one screen to display coffee machines and one screen to display coffee pods. On the coffee
machines screen, the user may filter by product type and water line. On the coffee pods screen, the user may filter by product type, coffee flavor, and pack size. Your task is to simulate this environment and build an API to return the data for these two screens.

### How to run ?
- make sure that mongodb local server is running
- pip3 install -r requirements.txt
- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 manage.py runserver

### Tools 
- Django
- Djongo (for managing Mongodb)
- Django-filter (for filtering coffee machines and coffee pods)
- Django restframework (for making RESTful API)

### Endpoints

- to get all coffee pods 
```sh
http://127.0.0.1:8000/api/v1/all-coffee-pods
```

- to get all coffee machines 
```sh
http://127.0.0.1:8000/api/v1/all-coffee-machines
```

- filter the small pods 
```sh
http://127.0.0.1:8000/api/v1/all-coffee-pods?product_type=CPS&coffee_flavor=&pack_size=
```

- filter small coffees pods with vanilla falvor 
```sh
http://127.0.0.1:8000/api/v1/all-coffee-pods?product_type=CPS&coffee_flavor=VA&pack_size=
```
- filter large machine coffees
```sh
http://127.0.0.1:8000/api/v1/all-coffee-machines?product_type=CML&product_model=&water_line_compatible=
```
