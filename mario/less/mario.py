# mario half pyramid
from cs50 import get_int

# asking user for input between 1 and 8
while True:

    # using get_int from cs50 library
    n = get_int("Enter the pyramid-height: ")
    if n > 0 and n < 9:
        break

# drawing right side pyramid
for i in range(n):
    print(" " * (n - 1 - i), end="")
    for j in range(i+1):
        print("#", end="")
    print()