def title_decorator(print_name_function):
  def wrapper(*args, **kwargs):
    print("Group 1:")
    print_name_function(*args, **kwargs)
  return wrapper

@title_decorator
def print_my_name(name, age):
  print(name + " you are " + str(age))

print_my_name("Jake", 32)
