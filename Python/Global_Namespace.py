print(' -- Globals Namespace with empty script -- \n')
# Write Checkpoint 1 here: 
print(globals())


# Write Checkpoint 2 here: 
global_variable = 'global'



# Write Checkpoint 3 here: 
def print_global():
  global_variable = 'nested global'
  nested_variable = 'nested value'



print(' \n -- Globals Namespace non-empty script -- \n')
# Write Checkpoint 4 here: 
print(globals())
