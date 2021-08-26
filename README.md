## Django Rest API + Google Maps ##
![](https://img.shields.io/badge/Python-3.8.5-blue.svg)
![](https://img.shields.io/badge/Django-3.2.6-blue.svg)
![](https://img.shields.io/badge/DjangoRestFramework-3.12.2-blue.svg)


### How to run
1. Create a virtual environment with Python 3.8.x
2. Activate virtualenv.
3. Create your .env file
4. Install dependencies
5. Run migrations
6. Run tests
7. Start server
8. Run command line to import data


#### Create a virtual environment


#### Create your .env file

Copy file .env_sample as .env and put your information ins this new file


#### Install dependencies

```
pip install -r requirements.txt
```


#### Running Migrations

```
python manage.py migrate
```

#### Running Tests

```
python manage.py test
```

Running Coverage

```
coverage run --source='.' manage.py test
```
To create HTML Coverage report
```
coverage html
```

#### Loading Customer Data

Be sure that the file is in folder contrib.

```
python manage.py load_csv customer.csv
```


#### How to start server

Open a terminal and type this code. The terminal must be in the folder where file ```manage.py``` is.
```
python manage.py runserver 0.0.0.0:8000
```

#### How to access Swagger Documentation

Open a browser in this url: ```http://0.0.0.0:8000```

#### Authentication

This project doesn't use authentication method. If you need this, change the value ```"DEFAULT_AUTHENTICATION_CLASSES"``` in settings.py

Example:
```
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 15,
    "DATE_INPUT_FORMATS": ["%d/%m/%Y", "%Y/%m/%d", "%d-%m-%Y", "%Y-%m-%d"],
    "DEFAULT_AUTHENTICATION_CLASSES": ["rest_framework.authentication.TokenAuthentication"],
    "DEFAULT_PERMISSION_CLASSES": [],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

```