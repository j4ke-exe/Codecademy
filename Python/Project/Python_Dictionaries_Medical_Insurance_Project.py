# Add your code here
medical_costs = {}
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3325.0
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})

total_cost = 0
for cost in medical_costs.values():
    total_cost += cost

# Create a variable to calculate average cost
average_cost = total_cost / len(medical_costs)
print(f"Average Insurance Cost: {average_cost}")

names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

# Zip names and ages
zipped_ages = zip(names, ages)
names_to_ages = {key: value for key, value in zipped_ages}

# Get the age of Marina
marina_age = names_to_ages.get("Marina", None)
print(f"Marina's age is {marina_age}")

# Create a list for medical records
medical_records = {}

medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-Smoker", "Insurance_cost": 6607.0}

medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-Smoker", "Insurance_cost": 3225.0}

medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-Smoker", "Insurance_cost": 8886.0}

medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}

medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Smoker", "Insurance_cost": 6420.0}

# Access specific piece of data in Connie's medical records
print("Connie's insurance cost is", str(medical_records["Connie"]["Insurance_cost"]), "dollars.")

# Remove Vinay's medical records
medical_records.pop("Vinay")

# Print a snapshot of each patient's medical record
for name, record in medical_records.items():
    print(name, "is a", str(record["Age"]), \
    "year old", record["Sex"], "-", record["Smoker"] \
    , "with a BMI of", str(record["BMI"]), \
    "and insurance cost of", str(record["Insurance_cost"]))
