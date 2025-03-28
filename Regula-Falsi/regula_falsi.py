def f(x):
    return x**3 - 4*x - 9  # Define the function

def find_interval(a, b, step):
    while f(a) * f(b) >= 0:
        a += step
        b += step
    
    return a, b

def regula_falsi(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Invalid initial interval: f(a) and f(b) must have opposite signs.")

    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))  # False position formula
        
        if abs(f(c)) < tol:  # Check convergence
            return c

        # Update interval
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    raise ValueError("Max iterations reached without convergence.")

initial_a = 0.0
initial_b = 1.0
step = 0.1

a, b = find_interval(initial_a, initial_b, step)
root = regula_falsi(a, b)
print(f"Root: {root:.6f}")
