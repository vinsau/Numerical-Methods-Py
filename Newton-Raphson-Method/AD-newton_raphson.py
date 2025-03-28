import autograd.numpy as np
from autograd import grad

# Define the function whose root we want to find
def f(x):
    return np.exp(x) + (2 ** -x) + (2 * np.cos(x)) - 6 # <<<<--- Modify this part

# Automatically compute the derivative of f(x)
df = grad(f)

# Newton-Raphson method for finding roots
def newton_method(x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)  # Evaluate function
        dfx = df(x)  # Evaluate derivative
        print(f"{i}: x:{x} || f(x):{fx} || f'(x):{dfx}")
        
        if np.abs(fx) < tol:  # Check convergence
            return x
        if dfx == 0:  # Avoid division by zero
            raise ValueError("Derivative is zero, Newton's method fails.")
        
        x = x - (fx / dfx)  # Newton's update step
    
    raise ValueError("Max iterations reached without convergence.")

# Example usage
initial_guess = 0.0
root = newton_method(initial_guess)
print(f"Root: {root:.6f}")
