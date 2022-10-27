# Import Decimal
from decimal import Decimal

# Fix the floating point math
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

# Output:
# 0.89
# 0.3445
