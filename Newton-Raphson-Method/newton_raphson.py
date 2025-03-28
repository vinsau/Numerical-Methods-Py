import math

def f(x):
    return math.exp(x) + (2 ** -x) + (2 * math.cos(x)) - 6

def df(x):
    return math.exp(x) - math.log(2) * (2 ** -x) - (2 * math.sin(x))

def newton_method(x0, tol=1e-6, max_iter=100):
    x = x0 # 2
    
    for i in range(max_iter):
        fx = f(x) 
        dfx = df(x) 
        
        print(f"{i}: x:{x} || fx:{fx} || dfx:{dfx}")

        if abs(fx) < tol:
            return x
        
        if dfx == 0:
            raise ValueError("Derivative is zero, Newton's method fails.")

        x = x - (fx / dfx)  # Newton's update step
        # 2 - (-9) / 8

    raise ValueError("Max iterations reached without convergence.")

# Example usage:
initial_guess = 0.0
root = newton_method(initial_guess)
print(f"Root: {root:.6f}")
