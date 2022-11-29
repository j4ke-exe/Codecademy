clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]

# Write your code below!
from collections import namedtuple

ClothingItem = namedtuple('ClothingItem', ['type', 'color', 'size', 'price'])

new_coat = ClothingItem('coat', 'black', 'small', 14.99)

# .price is called from the created namedtuple 'ClothingItem'
coat_cost = new_coat.price

updated_clothes_data = []
for i in clothes:
  # i[0] through i[3] are elements from the ClothingItem tuple
  updated_clothes_data.append(ClothingItem(i[0], i[1], i[2], i[3]))
  
print(updated_clothes_data)
