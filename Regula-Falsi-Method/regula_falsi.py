# REGULA FALSI METHOD
# Author: gauciv

import math
import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")  # Command for clearing the screen on Windows
    else:
        os.system("clear")  # Command for clearing the screen on Linux/macOS

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
    clear_screen()
    print(f"{'[REGULA FALSI]':>30}")
    # Ensure the initial interval is valid
    if f(a) * f(b) >= 0:
        raise ValueError("Invalid initial interval: f(a) and f(b) must have opposite signs.")
    
    print("-" * 47)

    for i in range(max_iter):
        # Compute the false position using linear interpolation
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        print(f"| {i+1:>2} | c = {c:12.6f} | f(c) = {f(c):12.6f} |")

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
initial_a = 0.0
initial_b = 1.0
step = 0.1

# Find a valid interval and compute the root
a, b = find_interval(initial_a, initial_b, step)
root = regula_falsi(a, b)
print("-" * 47)
print(f"Interval: a = {a:.6f} and b = {b:.6f}")
print(f"\nRoot: {root:.6f}")
print("=" * 14)
