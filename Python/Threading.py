import time
import threading
def greeting_with_sleep(string):
  s = time.perf_counter()
  print(string)
  time.sleep(2)
  print("says hello!")
  elapsed = time.perf_counter() - s
  print("Sequential Programming Elapsed Time: " + str(elapsed) + " seconds")

t = threading.Thread(target=greeting_with_sleep, args=('Codecademy',))
t.start()
