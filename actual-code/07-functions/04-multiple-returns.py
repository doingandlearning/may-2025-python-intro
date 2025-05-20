import random
import math
def analyse_counts(signal, background):
    """
    This function calculates the total noise and the percentage of signal of the total
    :param signal: the magnitude of the signal
    :param background: the magnitude of the background
    :return: total noise and the purity percentage
    """
    total = signal + background

    if total == 0:
        purity = 0
    else:
        purity = signal / total

    return total, purity

print(analyse_counts(43, 12))
print(random.randint(1, 10))
print(math.factorial(10))
# print(random.)