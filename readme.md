# Django Local library project

## Prerequisites

1. Install [Django3.1](https://docs.djangoproject.com/en/3.1/intro/install/) or above.
2. Install [python3.1](https://www.python.org/downloads/) or above.

## Installation
1. Clone this [repository](https://github.com/Testpress-Work/locallibrary).
2. Configure database if required.
3. Install required depedencies from:
```python
pip install -r requirement.txt
```
4. Run makemigrations & migrate commands.
```python
python manage.py makemigrations
python manage.py migrate
```
5. Create superuser if required.
```python
python manage.py createsuperuser
```
6. Run development server.
```python
python manage.py runserver
```
7. Open your web browser & go to `localhost:8000`
8. That's all. Cheers!