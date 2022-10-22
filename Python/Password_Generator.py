def password_generator(first, last):
  random = first[:3] + last[:4]
  return random
random = password_generator("dF09%&^!l_", "$^!@#%12faZ")
print(random)

def shuffle(pass_word):
    password = ""
    for i in range(0, len(pass_word)):
        password += pass_word[i-1]
    return password
password = shuffle(random)
print(password)
