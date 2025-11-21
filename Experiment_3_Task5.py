# Import the random and math modules.
# Generate a random number between 1 and 100 using random.randint().
# Use the math module to check if the number is prime (a prime number is a number greater than 1 that has no divisors other than 1 and itself).
# Print whether the random number is prime or not.

import random
import math

def is_prime(n):
    if n <= 1:
        return False
    # Only need to check divisors up to the square root of n
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

# Generate a random number between 1 and 100
num = random.randint(1, 100)

# Check if it is prime
print('-'*40)
if is_prime(num):
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")

print('-'*40)
