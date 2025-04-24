# NEWTON-RAPHSON METHOD
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
    return math.exp(x) + (2 ** -x) + (2 * math.cos(x)) - 6 # <<<<--- Modify this part

# Manually compute the derivative of f(x)
def df(x):
    return math.exp(x) - math.log(2) * (2 ** -x) - (2 * math.sin(x)) # <<<<--- Modify this part

# Newton-Raphson method for finding roots
def newton_method(x0, tol=1e-6, max_iter=100):
    x = x0
    clear_screen()
    print(f"{'[NEWTON-RAPHSON]':>42}")
    print("-" * 69)

    for i in range(max_iter):
        fx = f(x)  # Evaluate function
        dfx = df(x)  # Evaluate derivative
        
        print(f"| {i+1:>2} | x = {x:12.6f} | f(x) = {fx:12.6f} | df(x): {dfx:12.6f} |")


        if abs(fx) < tol:  # Check convergence
            return x
        
        if dfx == 0:  # Avoid division by zero
            raise ValueError("Derivative is zero, Newton's method fails.")

        x = x - (fx / dfx)  # Newton's update step

    raise ValueError("Max iterations reached without convergence.")

# Example usage
initial_guess = 5.0
root = newton_method(initial_guess)

print("-" * 69)
print(f"\nRoot: {root:.6f}")
print("=" * 14)
