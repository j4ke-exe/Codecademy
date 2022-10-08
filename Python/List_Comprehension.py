# List comprehension
grades = [90, 88, 62, 76, 74, 89, 48, 57]

# 10 gets added to every grade (num) from the grade list (grades)
scaled_grades = [num + 10 for num in grades]

# Sort grades in descending order
scaled_grades.sort(reverse=True)

# Print grades
print(scaled_grades)
