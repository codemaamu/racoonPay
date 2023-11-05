from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from urllib.parse import unquote
app = Flask(__name__)


# Create a connection to the database
conn = sqlite3.connect('users.db')
cur = conn.cursor()

# Create a table if it does not exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS users 
    (username TEXT, userAddress TEXT, password TEXT)
''')
conn.commit()


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    connect = sqlite3.connect('users.db') 
    cursor = connect.cursor() 
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    if user:
        return redirect(url_for('transIndex',user=user))
    else:
        return render_template('login.html', error='Invalid username or password')
     

@app.route('/transIndex/<user>')
def transIndex(user):
    data_string = (str)(user)
    decoded_string = unquote(data_string)
# Remove the parentheses and split the string to get individual values
    values = decoded_string.strip("()").split(", ")
    name = values[0].strip("'")
    walletaddress = values[1].strip("'")
    password = values[2].strip("'")
    if user:
        return render_template('transIndex.html',name=name,walletaddress=walletaddress)
    else:
        return render_template('login.html',"Error")


if __name__ == '__main__':
    app.run(debug=True)
