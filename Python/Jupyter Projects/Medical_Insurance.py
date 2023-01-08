medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Replace # with $
updated_medical_data = medical_data.replace('#', '$')

# Count the number of records in the data
num_records = 0
for character in updated_medical_data:
    if character == "$":
        num_records += 1

# Print the number of records
print(f"There are {num_records} medical records in the data.\n")

# Split the medical data into a list of records
medical_data_split = updated_medical_data.split(";")

# Split each record into a list of items
medical_records = []
for record in medical_data_split:
  medical_records.append(record.split(','))

# Remove leading and trailing whitespace from each item
medical_records_clean = []
for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)

# Capitalize the names of the patients
for record in medical_records_clean:
  record[0] = record[0].upper()
  print(record[:-1])

# Extract the data from the medical records
names = []
ages = []
bmis = []
insurance_costs = []
for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])

# Print the extracted data
print(f"\nNames: {names}\n")
print(f"Ages: {ages}\n")
print(f"BMIs: {bmis}\n")
print(f"Insurance Costs: {insurance_costs}\n")

# Calculate the average BMI
total_bmi = 0
for bmi in bmis:
  total_bmi += float(bmi)
average_bmi = total_bmi / len(bmis)

# Format the average BMI to two decimal places
average_bmi = "{:.2f}".format(average_bmi)

# Print the average BMI
print(f"Average BMI: {average_b
