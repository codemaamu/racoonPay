from web3 import Web3

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"  # Update with your Ganache URL
w3 = Web3(Web3.HTTPProvider(ganache_url))
from flask import Flask, render_template, request, redirect, url_for, session,g
import sqlite3



app = Flask(__name__)

app.secret_key = 'mysession'

def get_db_connection():
    conn = getattr(g, '_database', None)
    if conn is None:
        conn = g._database = sqlite3.connect('userdata.db')
    return conn
def getUser():
    g.user = 'Im global bitch' 

    return g.user

@app.route('/thisbs')
def bs():
    print(app.url_map)
    print("Fuck")
    return "ommala"

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = get_db_connection()
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    session['currentuser'] = user[0]
    session['currentaddress'] = user[1]
    if user:
       return redirect(url_for('transIndex'))
    else:
       return render_template('login.html', error='Invalid username or password')
     

@app.route('/transIndex')
def transIndex():

    return render_template('transIndex.html',user=session.get("currentuser","sessionerror"),currentaddress=session.get("currentaddress","sessionerror"))
   

    
    
@app.route('/paycon')
def uPayCon():
    conn = get_db_connection()
    cursor = conn.cursor() 
    tag = 'N'
    cursor.execute("SELECT * FROM users WHERE tag=?", (tag))
    user = cursor.fetchall()
    print(user)
    names_and_addresses = [(item[0], item[1]) for item in user for _ in range(1)]

    print(names_and_addresses)
    receivername =[]
    receiveraddress = []
    receivername = [item[0] for item in names_and_addresses]
    receiveraddress = [item[1] for item in names_and_addresses]

    print("Done till here")
    print(receivername)
    print(receiveraddress)
    return render_template('paycon.html',user=session.get("currentuser","sessionerror"),currentaddress=session.get("currentaddress","sessionerror"),receivername=receivername,receiveraddress=receiveraddress)
    
@app.route("/transact")
def payment():
    ganache_url = "http://127.0.0.1:7545"  # Update with your Ganache URL
    w3 = Web3(Web3.HTTPProvider(ganache_url))

    user=session.get("currentuser","sessionerror")
    currentaddress=session.get("currentaddress","sessionerror")
    receivername=session.get("receivername","sessionerror")
    receiveraddress=session.get("receiveraddress","sessionerror")
    ethvalue=session.get("EthValue","sessionerror")

    #receivername = request.form[]
# Example: Send Ether from one address to another
    user 
    transaction = {
    'from': currentaddress,  # Replace with your sender address
    'to': receiveraddress,  # Replace with the receiver's address
    'value': w3.to_wei(ethvalue, 'ether'),
    'gas': 2000000,
    'gasPrice': w3.to_wei('50', 'gwei'),
    'nonce': w3.eth.get_transaction_count(currentaddress),
    }

    tx_hash = w3.eth.send_transaction(transaction)
    print(tx_hash)
    print(f"Transaction Hash: {tx_hash.hex()}")
    session["tx_hash"] = tx_hash.hex()
    if tx_hash:
        return redirect(url_for("successfu"))
    
@app.route("/successfu/")
def successfu():
    return render_template("successfu.html",tx_hash=session.get("tx_hash","SessionError"))

@app.route("/Confirmation", methods = ['POST'])
def confirmpayment():

    receivername = request.values['name']
    receiveraddress = request.values['address']
    EthValue = request.values['ethvalue']
    print(receiveraddress)
    print(EthValue)
    print(receivername)
    session['receiveraddress'] = receiveraddress
    session['receivername'] = receivername
    session['EthValue'] = EthValue
    return redirect(url_for('danger'))

@app.route("/danger/")
def danger():
    return render_template('danger.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    

