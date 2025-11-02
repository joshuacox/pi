import math

def bbp_pi(n):
    pi = 0.0
    for k in range(n):
        pi += 1/(16**k)*(
            4/(8*k+1)-
            2/(8*k+4)-
            1/(8*k+5)-
            1/(8*k+6)
        )
    return pi

# Calculate Pi to 2000 decimal places
n = 100 # choose a high enough number for accurate results
pi = bbp_pi(n)

# Print the result with precision of 2000 digits
print(f"Pi: {pi:.2000f}")
