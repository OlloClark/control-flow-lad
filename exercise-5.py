# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

x = 1
y = 1

for n in range(0, 50):
    if n == 0:
        x = 0
        print(f"term: {n} / number {x}")
    elif n == 1:
        y = 1
        print(f"term: {n} / number {y}")
    else:
        z = x + y
        print(f"term: {n} / number {z}")
        x = y
        y = z