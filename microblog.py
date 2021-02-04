from app import app, db
from app.models import User, Post

# `flask shell` in the terminal
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
