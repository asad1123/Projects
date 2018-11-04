from math import atan

# Ensure integer input
num_digits = None
while (num_digits is None):
    try:    
        num_digits = int(input('How many digits should Pi have? '))
    except ValueError:
        print('Please enter a valid integer.')

# Cap number of digits to 0 <= n <= 40
if num_digits < 0:
    num_digits = 0
if num_digits > 40:
    num_digits = 40

# Euler's method for computing pi
pi = 20 * atan(1.0 / 7.0) + 8 * atan(3.0 / 79.0)

# Print pi up to `num_digit` digits
print('{:.{}f}'.format(pi, num_digits))