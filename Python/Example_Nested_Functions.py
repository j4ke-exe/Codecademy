# Example of nested functions and scope
def outer_func():
  location = "Inside the outer function."
  
  def inner_func():
    location = "Inside the inner function."
    print(location)
    
  inner_func()
  
  print(location)

outer_func()
