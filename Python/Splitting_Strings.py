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
