## Django Rest API + Google Maps ##
![](https://img.shields.io/badge/Python-3.8.5-blue.svg)
![](https://img.shields.io/badge/Django-3.2.6-blue.svg)
![](https://img.shields.io/badge/DjangoRestFramework-3.12.2-blue.svg)


## Create a virtual enviroment


## Create your .env file

Copy file .env_sample as .env and put your information ins this new file


## Install requirements

```
pip install -r requirements.txt
```


## Running Migrations

```
python manage.py migrate
```

## Running Tests

```
python manage.py test
```

Running Coverage

```
coverage run --source='.' manage.py test
coverage html
```