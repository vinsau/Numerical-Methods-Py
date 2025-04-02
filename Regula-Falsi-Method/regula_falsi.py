import math

# Define the function whose root we're finding
def f(x):
    return math.exp(x) + (2 ** -x) + (2 * math.cos(x)) - 6

# Shift interval until f(a) and f(b) have opposite signs
def find_interval(a, b, step):
    while f(a) * f(b) >= 0:
        a += step
        b += step
    return a, b

# Regula Falsi (False Position) method for root finding
def regula_falsi(a, b, tol=1e-6, max_iter=100):
    # Ensure the initial interval is valid
    if f(a) * f(b) >= 0:
        raise ValueError("Invalid initial interval: f(a) and f(b) must have opposite signs.")

    for i in range(max_iter):
        # Compute the false position using linear interpolation
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        print(f"{i+1}: f(a): {f(a)}    |   f(b): {f(b)}    |   f(c): {f(c)} ")
        # If the function value is close enough to zero, return the root
        if abs(f(c)) < tol:
            return c

        # Narrow down the interval where the sign changes
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    raise ValueError("Max iterations reached without convergence.")

# Initial guesses and step for finding a valid interval
initial_a = 1.0
initial_b = 2.0
step = 0.1

# Find a valid interval and compute the root
a, b = find_interval(initial_a, initial_b, step)
root = regula_falsi(a, b)
print(f"Root: {root:.6f}")
