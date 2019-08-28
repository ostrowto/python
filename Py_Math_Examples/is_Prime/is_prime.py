# Is prime

import math

def is_Prime(number: int) -> bool:
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, 1+int(math.sqrt(number)), 2):
        if number % i == 0:
            return False
    return True
