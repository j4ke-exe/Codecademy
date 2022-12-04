import time
import threading
def greeting_with_sleep(string):
  print(string)
  time.sleep(2)
  print("says hello!")

def main_threading():
  s = time.perf_counter()
  greetings = ['Codecademy', 'Chelsea', 'Hisham', 'Ashley']
  # your code goes here
  for i in range(len(greetings)):
    t = threading.Thread(target=greeting_with_sleep, args=(greetings[i],))
    t.start()
  elapsed = time.perf_counter() - s
  print("Threading Elapsed Time: " + str(elapsed) + " seconds")

main_threading()
