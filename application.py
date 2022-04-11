from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
# import mysqldb.cursors
import re
import mysql.connector
import pymysql as MySQLdb


app = Flask(__name__)

app.secret_key = 'abcd'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'login'

mysql = MySQL(app)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    print("hi")
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        print("hi")
        print(username)
        print(password)
        '''cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s  AND password = % s', (username, password))
        accounts = cursor.fetchone()'''
        conn = MySQLdb.connect(
            host='localhost',
            user='root',
            password="root",
            db='login',
        )
        cur = conn.cursor()
        # Select query
        cur.execute('SELECT * FROM signup WHERE username = % s  AND password = % s', (username, password))
        accounts = cur.fetchone()
        print(accounts)
        if accounts:
            session['loggedin'] = True
            session['username'] = username
            msg = 'Logged in successfully !'
            return render_template('insert.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/templates/signup.html', methods=['GET', 'POST'])
def signup():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'email' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        print("hi")
        #print(username)
        #print(email)
        #print(password)

        '''cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM signup WHERE id = % s', (username, email, password))
        signup = cursor.fetchone()'''
        conn = MySQLdb.connect(
            host='localhost',
            user='root',
            password="root",
            db='login',
        )
        cur = conn.cursor()
        # Select query
        cur.execute('SELECT * FROM signup WHERE username = % s and email = % s AND password = % s', (username, email, password))
        signup = cur.fetchone()
        print(signup)
        if signup:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cur.execute('INSERT INTO signup VALUES (NULL, % s, % s, % s)', (username, password, email))
            #signup = cur.fetchone()
            conn.commit()
            msg = 'You have successfully signedUp !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('signup.html', msg=msg)


@app.route("/templates/about.html")
def about():
    return render_template("about.html")


@app.route("/templates/login.html")
def index():
    return render_template("login.html")


'''
@app.route('/')
def home():
    return render_template('login.html')



@app.route("/templates/signup.html")
def signup():
    return render_template("signup.html")
'''

if __name__ == '__main__':
    app.run(debug=True, port=9300)
