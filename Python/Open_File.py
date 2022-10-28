with open('welcome.txt') as text_file:
  text_data = text_file.read()
print(text_data)

#-------------------------------------

# Iterate through each line and assign it to a variable.
with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)

#-------------------------------------

# Read line by line
with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
print(first_line)
