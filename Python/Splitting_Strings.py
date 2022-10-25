authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

# Remove the commaas
author_names = authors.split(',')
print(author_names)

# Only print Authors last name
author_last_names = []
for name in author_names:
  # Split [-1] = first name and append only last name
  author_last_names.append(name.split()[-1])
print(author_last_names)

#----------------------------------------------------

# Splitting and joining lines
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)
