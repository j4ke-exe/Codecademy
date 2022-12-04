import sqlite3

con = sqlite3.connect("titanic.db")
curs = con.cursor()

# Pull the Age records from the titanic table using .fetchall() method and save as age
age = curs.execute("SELECT Age FROM titanic;").fetchall()

# Create a for loop that calculates the number of children
sum = 0
for num in age: 
  if num[0] < 18:
    sum = sum + 1
            
print(sum)
