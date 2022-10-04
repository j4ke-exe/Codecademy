weight = 20
premium = 120

#Premium Shipping
if weight >= 21:
  print("Cost for premium shipping is " + "$" + str(premium))

#Ground Shipping
if weight <= 2:
  print("Ground shipping cost is " + "$" + str(weight*1.5+20))
elif weight > 2 and weight <= 6:
  print("Ground shipping cost is " + "$" + str(weight*3+20))
elif weight > 6 and weight <= 10:
  print("Ground shipping cost is " + "$" + str(weight*4+20))
else:
  print("Ground shipping cost is " + "$" + str(weight*4.75+20))

#Drone Shipping
if weight <= 2:
  print("Drone shipping cost is " + "$" + str(weight*4.5))
elif weight > 2 and weight <= 6:
  print("Drone shipping cost is " + "$" + str(weight*9))
elif weight > 6 and weight <= 10:
  print("Drone shipping cost is " + "$" + str(weight*12))
else:
  print("Drone shipping cost is " + "$" + str(weight*14.25))
