# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from contextlib import closing

# configuration
# for larger apps, cleaner to put this in a separate file, then import values from there
DATABASE = '/tmp/flaskr.db'
# never leave debug mode activated in production env
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our application
app = Flask(__name__)
app.config.from_object(__name__)

# from_object() looks at given object, then looks at all uppercase variables defined there
    # in this case, the configuration above
    # would use the following to load from separate file:

    # app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# initializes databse
def init_db():
    with closing(connect_db()) as db:
        # pulls in our schema table
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
# in terminal, start up python shell (type in python)
    # then type in the following:
        # from flaskr import init_db
        # init_db()
    # exit the shell with control-D or typing: exit()

# connects to database before each request
@app.before_request
def before_request():
    g.db = connect_db()

# prevents app from breaking if a request has an error
@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    # renders show_entries template and gives page access to data
    return render_template('show_entries.html', entries=entries)

# lets users add entries if logged in
@app.route('/add', methods=['POST'])
def add_entry():
    # checks if the logged_in key is present and True
    if not session.get('logged_in'):
        abort(401)
    # use question marks when building SQL statements for security
        # vulnerable to SQL injection otherwise
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    # redirect(url_for()) takes the name of a defined function
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            # bad logins display a message about the error
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            # sets logged_in key to True in session
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    # if not a POST request, GETs login page
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    # removes logged_in key if present, or does nothing if not logged in
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

# starts the server
if __name__ == '__main__':
    app.run()





















