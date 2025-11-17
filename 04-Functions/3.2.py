###
# Generates and prints a random number between 1 and 6,
# similar to rolling a dice
#
import random

for i in range(1, 7):
    random_num = random.randint(1,6)
    print(random_num, end=" ")