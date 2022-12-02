# Named Tuples
from collections import namedtuple

student = namedTuple("Student", ["name", "age", "grade"])

scott = student("Scott", 28, "A")
nicole = student("Nicole", 26, "B")
john = student("John", 29, "D")
