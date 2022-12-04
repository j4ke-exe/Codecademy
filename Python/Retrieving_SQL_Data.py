import sqlite3

con = sqlite3.connect("titanic.db")
curs = con.cursor()

# Pull the first row from the titanice data table (print to view output)
one = curs.execute("SELECT * FROM titanic").fetchone()
print(one)
# Pull the first ten rows from the titanice data table (print to view output)
ten = curs.execute("SELECT * FROM titanic").fetchmany(10)
print(ten)
# Pull every row from the titanice data table (print to view output)
all_rows = curs.execute("SELECT * FROM titanic").fetchall()
print(all_rows)
# Pull every row from the titanice data table for those who survived (print to view output)
all_survived = curs.execute('''SELECT * FROM titanic WHERE Survived = 1;''').fetchall()
print(all_survived)
