import math

# Define the function whose root we're finding
def f(x):
    return math.exp(x) + (2 ** -x) + (2 * math.cos(x)) - 6

# Secant method for finding the root of f(x)
def secant_method(x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        # Avoid division by zero
        if f_x1 - f_x0 == 0:
            raise ValueError("Division by zero encountered in secant method.")
        
        # Compute new approximation using secant formula
        x2 = x1 - f_x1 * ((x1 - x0) / (f_x1 - f_x0))
        
        print(f"{i + 1}: x2= {x2}  | f(x2)= {f(x2)}")
        
        # Check if the result is within the tolerance
        if abs(f(x2)) < tol:
            return x2
        
        # Update previous approximations for next iteration
        x0, x1 = x1, x2
    
    raise ValueError("Max iterations reached without convergence.")

initial_x0 = 0.0  # First initial guess
initial_x1 = 1.0  # Second initial guess

root = secant_method(initial_x0, initial_x1)
print(f"Root: {root:.6f}")
