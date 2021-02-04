### followed

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

### how to run

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install flask
$ pip install flask-wtf

$ pip install flask-sqlalchemy
$ pip install flask-migrate
$ flask db init
$ flask db migrate -m "users table"
$ flask db upgrade
$ flask db migrate -m "posts table"
$ flask db upgrade

$ flask run
```
