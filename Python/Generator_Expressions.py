def cs_generator():
  for i in range(1, 5):
    yield "Computer Science " + str(i)

print("Regular For Loop")
print("-----------------------")
cs_courses = cs_generator()
for course in cs_courses:
  print(course)

print("\n")

print("Generator Comprehension")
print("-----------------------")
cs_generator_exp = ("Computer Science {}".format(i) for i in range(1, 5))
for course in cs_generator_exp:
  print(course)
