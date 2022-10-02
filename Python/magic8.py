import random

random_number = random.randint(1, 9)
# print(random_number) # Test random_randint function

question = "Will it rain today?"
name = "Jake"

if len(question) == 0:
  print("You must provide a question for me to answer.")
elif len(name) == 0:
  print("Question:", question)
else:
  print(name + " asks: " + question)

if random_number == 1:
  print("Yes - definitely!")
elif random_number == 2:
  print("It is decidedly so.")
elif random_number == 3:
  print("Without a doubt!")
elif random_number == 4:
  print("Reply hazy, try again.")
elif random_number == 5:
  print("Ask again later.")
elif random_number == 6:
  print("Better not tell you now.")
elif random_number == 7:
  print("No.")
elif random_number == 8:
  print("Does not look so good.")
elif random_number == 9:
  print("Very unlikely.")
else:
  print("Error! Try again.")
