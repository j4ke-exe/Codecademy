def times3(a, b, function):
  return 3 * function(a, b)
 
add_then_times3 = times3(2, 4, lambda x, y: x + y) # 18
sub_then_times3 = times3(2, 4, lambda x, y: x - y) # -6
