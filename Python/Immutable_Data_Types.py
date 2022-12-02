# Named Tuples
from collections import namedtuple

student = namedtuple("Student", ["name", "age", "grade"])

scott = student("Scott", 28, "A")
nicole = student("Nicole", 26, "B")
john = student("John", 29, "D")

print(scott.name) # Scott
print(nicole.age) # 26
print(john.grade) # D

# Packaging student tuples into one
students = (scott, nicole, john)

# ---------------------------------
# Exercise 1
# Create a tuple for countries
# ---------------------------------
from collections import namedtuple

# Checkpoint 1 code goes here.
country = namedtuple("Country", ["name", "capital", "continent"])
# Checkpoint 2 code goes here.
france = country("France", "Paris", "Europe")
japan = country("Japan", "Tokyo", "Asia")
senegal = country("Senegal", "Dakar", "Africa")
# Checkpoint 3 code goes here.
countries = (france, japan, senegal)

print(countries)
