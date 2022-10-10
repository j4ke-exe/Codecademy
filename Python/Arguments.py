# Set function definition to trip_planner with 3 arguments
def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

trip_planner("France", "Germany", "Denmark")

trip_planner("Denmark", "France", "Germany")

# Define keyword arguments
trip_planner(first_destination = "Iceland", second_destination = "India", final_destination = "Germany")

# Test default argument to see if Codecademy HQ prints
trip_planner("Brooklyn", "Queens")
