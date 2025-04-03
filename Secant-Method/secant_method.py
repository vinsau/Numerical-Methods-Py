# SECANT METHOD
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

# Define the function whose root we're finding
def f(x):
    return math.exp(x) + (2 ** -x) + (2 * math.cos(x)) - 6

# Secant method for finding the root of f(x)
def secant_method(x0, x1, tol=1e-6, max_iter=100):
    clear_screen()
    print(f"{'[SECANT METHOD]':>30}")

    print("-" * 50)
    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        # Avoid division by zero
        if f_x1 - f_x0 == 0:
            raise ValueError("Division by zero encountered in secant method.")
        
        # Compute new approximation using secant formula
        x2 = x1 - f_x1 * ((x1 - x0) / (f_x1 - f_x0))
        
        print(f"| {i+1:>2} | x{i+2:2} = {x2:11.6f} | f(x{i+2:2}) = {f(x2):12.6f} |")
        
        # Check if the result is within the tolerance
        if abs(f(x2)) < tol:
            return x2
        
        # Update previous approximations for next iteration
        x0, x1 = x1, x2
    
    raise ValueError("Max iterations reached without convergence.")

initial_x0 = 0.0  # First initial guess
initial_x1 = 1.0  # Second initial guess

# gimmicks()

root = secant_method(initial_x0, initial_x1)
print("-" * 50)
print(f"\nRoot: {root:.6f}")
print("=" * 14)
