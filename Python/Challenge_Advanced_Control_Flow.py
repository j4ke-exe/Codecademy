# Advanced challenges that tests if numbers fall within specified ranges and prints the result
def in_range(num, lower, upper):
    if (num >= lower) and (num <= upper):
        return True
    else:
        return False
# Prints False
print(in_range(5, 10, 20))
# Prints True
print(in_range(10, 10, 10))
#---------------------------------------------
def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False
# Prints False
print(same_name("Tina", "Amber"))
# Prints True
print(same_name("Colby", "Colby"))
#---------------------------------------------
def always_false(num):
    if (num != 0) and (num == 0):
        return True
    else:
        return False
# Prints False
print(always_false(0))
print(always_false(-1))
print(always_false(1))
#---------------------------------------------
def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    if rating < 9:
        return "This one was fun."
    return "Outstanding!"
# Prints "Outstanding!"
print(movie_review(9))
# Prints "Avoid at all costs!"
print(movie_review(4))
# Prints "This one was fun."
print(movie_review(6))
#---------------------------------------------
def max_num(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        return num1
    if (num2 > num1 and num2 > num3):
        return num2
    if (num3 > num1 and num3 > num2):
        return num3
    else:
        return "It's a tie!"
# Prints 10
print(max_num(-10, 0, 10))
# Prints 5
print(max_num(-10, 5, -30))
# Prints -5
print(max_num(-5, -10, -10))
# Prints It's a tie!
print(max_num(2, 3, 3))
