global_variable = 'global'
 
def outer_function():
  outer_value = "outer"
 
  def inner_function():
    inner_value = "inner"

    def inner_nested_function():
      nested_value = 'nested'
    inner_nested_function()
    # Add locals() below
    print(locals())
  inner_function()
 
outer_function()

#-------------------------------

def calc_paint_amount(width, height):

  square_feet = width * height
  def calc_gallons():
    sqft_divided = square_feet / 400
    return sqft_divided
  return calc_gallons()

print('Number of paint gallons needed: ')
print(str(calc_paint_amount(30,20)))
