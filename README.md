# MovieDB
*Built with Django (v. 2.0.5), Django REST framework and Bootstrap*



Assuming that at least virtualenv is installed:

```
virtualenv env
source env/bin/activate
pip install django
pip install djangorestframework
```

+ if using default database with some examples:
```
python manage.py runserver
```
+ if setting up completely new database (first make sure that default DB is removed):
```
python manage.py migrate
```
```
python manage.py runserver
```

Heroku live preview: [Click](https://bkozlowski.herokuapp.com/), admin credentials: admin:asdasd123, access admin panel [here](https://bkozlowski.herokuapp.com/admin).

### API module:

Api is available under following links:

+ [api/movie](https://bkozlowski.herokuapp.com/api/movie) for movie GET request

+ [api/comment](https://bkozlowski.herokuapp.com/api/comment) for comment GET request

+ [api/movie/create](https://bkozlowski.herokuapp.com/api/movie) for POST movie request

+ [api/comment/create](https://bkozlowski.herokuapp.com/api/comment) for comment GET request
