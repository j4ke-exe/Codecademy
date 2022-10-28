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

#-------------------------------------

# Write to a file and read it
with open('bad_bands.txt', 'w') as bad_bands_doc:
  bad_bands_doc.write("Vanilla Ice")

with open('bad_bands.txt') as bad_bands_doc:
  file_read = bad_bands_doc.read()
print(file_read)
