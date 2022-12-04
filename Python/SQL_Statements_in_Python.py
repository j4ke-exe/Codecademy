from start import helper
helper()
import sqlite3

con = sqlite3.connect("titanic.db")
curs = con.cursor()

# Create table named new_table
curs.execute('''CREATE TABLE new_table (
                    name TEXT, 
                    age INTEGER, 
                    username TEXT, 
                    pay_rate REAL)''')
# Insert row of values into new_table
curs.execute('''INSERT INTO new_table VALUES ('Bob Peterson', 34, 'bob1234', 40.00)''')
