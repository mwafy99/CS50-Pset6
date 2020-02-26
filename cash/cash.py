# cash in python
from cs50 import get_float

while True:
    change = get_float("Change owed: ")
    if change > 0:
        break

# change from dollar to cents
cents = change * 100

# counting coins
coins = 0

# quarters
while cents >= 25:
    cents -= 25
    coins += 1

# dimes
while cents >= 10:
    cents -= 10
    coins += 1

# nickels
while cents >= 5:
    cents -= 5
    coins += 1

# pennies
while cents >= 1:
    cents -= 1
    coins += 1

# print the number of coins
print(coins)
