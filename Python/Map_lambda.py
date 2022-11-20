int_list = [3, 6, 9]

doubled = map(lambda input: input*2, int_list)

print(list(doubled))

#---------------------------------------------

grade_list = [3.5, 3.7, 2.6, 95, 87]

grades_100scale = map(lambda grade: grade*25 if grade <= 4.0 else grade, grade_list)

# convert grades_100scale to a list
updated_grade_list = list(grades_100scale)

print(updated_grade_list)
