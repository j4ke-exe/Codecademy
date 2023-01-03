# Add your code here
def analyze_smoker(smoker):
  if smoker == 1:
    print("To lower your cost, you should consider quitting smoking.\n")
  else:
    print("Smoking is not an issue for you.\n")

def analyze_bmi(bmi_value):
  if bmi_value > 30:
    print("Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI.\n")
  elif bmi_value >= 25 and bmi_value <= 30:
    print("Your BMI is in the overweight range. To lower your cost, you should lower your BMI.\n")
  elif bmi_value >= 18.5 and bmi_value < 25:
    print("Your BMI is in a healthy range.\n")
  else:
    print("Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.\n")

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.\n")
  analyze_smoker(smoker)
  analyze_bmi(bmi)
  return estimated_cost
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)

# -------------------------------

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.\n")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Add your code here
names = ['Maria', 'Rohan', 'Valentina']
insurance_costs = [4150.0, 5320.0, 35210.0]
insurance_data = list(zip(names, insurance_costs))

estimated_insurance_data = []
estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))
print(f'Here is the actual insurance cost data:', str(estimated_insurance_data))
