# THIS CODE AUTOMATICALLY DERIVES F WITH GRAD FUNCTION FROM AUTOGRAD
# NEWTON-RAPHSON METHOD
# Author: gauciv

import autograd.numpy as np
from autograd import grad
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

# Define the function whose root we want to find
def f(x):
    return np.exp(x) + (2 ** -x) + (2 * np.cos(x)) - 6 # <<<<--- Modify this part

# Automatically compute the derivative of f(x)
df = grad(f)

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

        
        if np.abs(fx) < tol:  # Check convergence
            return x
        if dfx == 0:  # Avoid division by zero
            raise ValueError("Derivative is zero, Newton's method fails.")
        
        x = x - (fx / dfx)  # Newton's update step
    
    raise ValueError("Max iterations reached without convergence.")

initial_guess = 5.0 # <<<<--- Modify this guess
gimmicks()
root = newton_method(initial_guess)
print("-" * 69)
print(f"\nRoot: {root:.6f}")
print("=" * 14)