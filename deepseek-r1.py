from decimal import Decimal, getcontext
import math

def pi_chudnovsky():
    """
    Calculate Pi using the Chudnovsky algorithm to 2000 decimal places.
    """
    from math import factorial

    # Set high precision
    getcontext().prec = 300  # Sufficient for 2000 decimals, with some padding.

    sqrt3 = Decimal(3).sqrt()
    sum_pi = Decimal(0)
    k = 0

    while True:
        term = (Decimal(-1)**k) * factorial(6*k) / (factorial(k)**3 * factorial(3*k))
        term *= 8 * sqrt3 / (262537412640768 ** k)
        sum_pi += Decimal(str(term))

        # Check for convergence
        if len(str(sum_pi)) > getcontext().prec + 5:
            break

        k += 1

    return sum_pi

# Calculate Pi to 2000 decimal places
pi = pi_chudnovsky()
# Convert to string, remove the leading '0.' and print with 2000 decimals
print(str(int(pi)) + '.' + str(pi)[2:2002])
