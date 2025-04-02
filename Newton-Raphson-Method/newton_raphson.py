# NEWTON-RAPHSON METHOD
# Author: gauciv

import math

# Define the function whose root we want to find
def f(x):
    return math.exp(x) + (2 ** -x) + (2 * math.cos(x)) - 6 # <<<<--- Modify this part

# Manually compute the derivative of f(x)
def df(x):
    return math.exp(x) - math.log(2) * (2 ** -x) - (2 * math.sin(x)) # <<<<--- Modify this part

# Newton-Raphson method for finding roots
def newton_method(x0, tol=1e-6, max_iter=100):
    x = x0  
    
    for i in range(max_iter):
        fx = f(x)  # Evaluate function
        dfx = df(x)  # Evaluate derivative
        
        print(f"{i}: x:{x} || fx:{fx} || dfx:{dfx}")

        if abs(fx) < tol:  # Check convergence
            return x
        
        if dfx == 0:  # Avoid division by zero
            raise ValueError("Derivative is zero, Newton's method fails.")

        x = x - (fx / dfx)  # Newton's update step

    raise ValueError("Max iterations reached without convergence.")

# Example usage
initial_guess = 0.0
root = newton_method(initial_guess)
print(f"Root: {root:.6f}")
