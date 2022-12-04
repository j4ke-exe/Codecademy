import time
import asyncio

async def greeting_with_sleep_async(string):
  print(string)
  await asyncio.sleep(2)
  print(string + " says hello!") 

async def main_async():
  s = time.perf_counter()
  greetings = [greeting_with_sleep_async('Codecademy'), greeting_with_sleep_async('Chelsea'), greeting_with_sleep_async('Hisham'), greeting_with_sleep_async('Ashley')]
  # your code goes here
  await asyncio.gather(*greetings)

  elapsed = time.perf_counter() - s
  print("Asyncio Elapsed Time: " + str(elapsed) + " seconds")

loop = asyncio.get_event_loop()
loop.run_until_complete(main_async())
