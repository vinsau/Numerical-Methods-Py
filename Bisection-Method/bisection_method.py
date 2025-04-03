# BISECTION METHOD
# Author: gauciv

import math
import time
import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")  # Command for clearing the screen on Windows
    else:
        os.system("clear")  # Command for clearing the screen on Linux/macOS

# Define the function whose root we want to find
def f(x):
    return math.exp(x) + (2 ** -x) + (2 * math.cos(x)) - 6

# Find a valid interval [a, b] where f(a) and f(b) have opposite signs
def find_interval(a, b, step):
    while f(a) * f(b) >= 0:  # Ensure the function changes sign in the interval
        a += step
        b += step
    return a, b

# Bisection method to find the root of f(x)
def bisection_method(a, b, tol=1e-6, max_iter=100):
    clear_screen()
    if f(a) * f(b) >= 0:
        raise ValueError("Invalid initial interval: f(a) and f(b) must have opposite signs.")
    
    print(f"{'[BISECTION]':>28}")
    print("-" * 48)

    for i in range(max_iter):
        c = (a + b) / 2  # Calculate midpoint

        print(f"| {i+1:>3} | c = {c:12.6f} | f(c) = {f(c):12.6f} |")

        if abs(f(c)) < tol:  # Check if f(c) is close to zero
            return c

        # Narrow down the interval
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    raise ValueError("Max iterations reached without convergence.")

# Just for fun
def gimmicks():
    def countdown(message, value, end = "[SUCCESS!]"):
        clear_screen()
        print(message)
        for i in range(value, 0, -1):
            print(i)
            time.sleep(0.5)
        
        print(end)
        
    countdown("Starting program...", 3)
    time.sleep(1)
    countdown("Declaring initial variables...", 3)
    time.sleep(1)
    countdown("Finding correct interval...", 3)
    time.sleep(1)
    countdown("Computing root...", 5)
    time.sleep(1)
    countdown("Preparing to display table...", 3)
    time.sleep(1)

# Default initial values
# No need to modify these values as this program automatically searches for the right interval
initial_a = 0.0
initial_b = 1.0
step = 0.1

gimmicks()

# Find a valid interval and compute the root
a, b = find_interval(initial_a, initial_b, step)
root = bisection_method(a, b)

# Result display
print("-" * 48)
print(f"Interval: a = {a:.6f} and b = {b:.6f}")
print(f"\nRoot: {root:.6f}")
print("=" * 14)