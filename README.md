# EMBL-EBI | Rest API

### Requirements
- Python 3.9
- Django 4.0.3
- Django REST Framework 3.13.1

### Installation

After cloned the repository, create a virtual environment to have a clean python installation.
You can do this by running the command
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

### Structure

Endpoint |HTTP Method | Result
--- | --- |---
`molecules` | GET | Get all molecules 
`molecules/:id` | GET | Get a single molecule by id
`activity/:id`| GET | Get activities by molecule id

### Pagination
The API supports pagination, by default responses have a page_size=10 and the maximum value of the page size is 1000
```
http http://127.0.0.1:8000/molecules?page=1&page_size=20"
http http://127.0.0.1:8000/activity?page=1&page_size=30"
```

### Run the API server

To start up Django's development server

```
python manage.py runserver
```

To start the server with docker
```
docker-compose up
```

