MAX_STUDENTS = 50

def get_student_ids():
  student_id = 1
  while student_id <= MAX_STUDENTS:
    n = yield student_id
    if n is not None:
      student_id = n
      continue
    student_id += 1

student_id_generator = get_student_ids()
for i in student_id_generator:
  if i == 1:
    i = student_id_generator.send(25)
  print(next(student_id_generator))
  print(i)

#---------------------------------
# Methods: throw()

def student_counter():
  for i in range(1,5001):
    yield i

student_generator = student_counter()
for student_id in student_generator:
  # Write your code below:
  if student_id > 100:
    student_generator.throw(ValueError, "Invalid student ID")
  print(student_id)

#---------------------------------
# Close Infinite Loop with Methods: close()

def generator():
  i = 0
  while True:
    try:
      yield i
    except GeneratorExit:
      print("Infinite Loop Detected. Closing!")
      break
    i += 1
 
my_generator = generator()
for item in my_generator:
  print(item)
  if item == 1:
    my_generator.close()

#---------------------------------
# Connecting Generators

def science_students(x):
  for i in range(1,x+1):
    yield i

def non_science_students(x,y):
  for i in range(x,y+1):
    yield i
  
# Write your code below
def combined_students():
  yield from science_students(5)
  yield from non_science_students(10,15)
  yield from non_science_students(25,30)

student_generator = combined_students()
for i in student_generator:
  print(i)
