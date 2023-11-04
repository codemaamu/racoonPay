import mysql.connector

# Function to create the database and tables
def setup_database():
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Loki12345'
    )
    
    if conn.is_connected():
        print("Connected to MySQL server.")
        
        # Create the RacoonPay database
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS RacoonPay")
        conn.commit()
        cursor.close()
        
        # Reconnect to the new database
        conn.database = "RacoonPay"
        
        # Create the Transaction table
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Transaction (
                id INT AUTO_INCREMENT PRIMARY KEY,
                SenderName VARCHAR(255),
                SAddress VARCHAR(255),
                ReceiverName VARCHAR(255),
                RAddress VARCHAR(255),
                Amount DECIMAL(10, 2),
                Date DATE
            )
        ''')
        conn.commit()
        cursor.close()
        
        # Create the NGOList table
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS NGOList (
                id INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255),
                LastTransactionDate DATE,
                HighestAmount DECIMAL(10, 2),
                Flag INT()
            )
        ''')
        conn.commit()
        cursor.close()
        
        conn.close()
    else:
        print("Failed to connect to MySQL server.")

# Function to handle a transferred transaction
def transferred(sender_name, s_address, receiver_name, r_address, amount, date):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Loki12345',
        database='RacoonPay'
    )
    
    if conn.is_connected():
        cursor = conn.cursor()
        
        # Insert transaction data into the Transaction table
        cursor.execute('''
            INSERT INTO Transaction (SenderName, SAddress, ReceiverName, RAddress, Amount, Date)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (sender_name, s_address, receiver_name, r_address, amount, date))
        
        # Update the NGOList table if needed
        cursor.execute('''SELECT Name FROM NGOList WHERE Name = %s''', (receiver_name,))
        result = cursor.fetchone()
        
        if result is not None and amount > :
            cursor.execute('''
                UPDATE NGOList
                SET LastTransactionDate = %s, HighestAmount = %s
                WHERE Name = %s
            ''', (date, amount, receiver_name))

        cursor.execute('''
            SELECT * FROM NGOList WHERE Name = %s
        ''', (receiver_name,))
        result = cursor.fetchone()
        
        if result is None:
            # If the receiver name is not in NGOList, insert it
            cursor.execute('''
                INSERT INTO NGOList (Name, LastTransactionDate, HighestAmount, Flag)
                VALUES (%s, %s, %s, %s)
            ''', (receiver_name, date, amount, 0))
        elif amount > result[3]:
            # If the new amount is greater than HighestAmount, update and increase Flag
            cursor.execute('''
                UPDATE NGOList
                SET LastTransactionDate = %s, HighestAmount = %s, Flag = Flag + 1
                WHERE Name = %s
            ''', (date, amount, receiver_name))
        conn.commit()
        cursor.close()
        conn.close()

# Create the database and tables
setup_database()

# Example usage of the 'transferred' function
if __name__ == '__main__':
    transferred(
        "John Doe",
        "0x1234567890abcdef",
        "Charity Organization",
        "0x9876543210fedcba",
        100.0,
        "2023-11-04"
    )
    print("Transaction data has been added to the database.")
