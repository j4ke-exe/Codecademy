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
