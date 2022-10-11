# Convert fahrenheit to celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
f_in_celsius = f_to_c(32)
c = round(f_in_celsius)
print("Temp in Celsius:", c)

# Convert celsius to fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
c_in_fahrenheit = c_to_f(32)
f = round(c_in_fahrenheit)
print("Temp in Fahrenheit:", f)
