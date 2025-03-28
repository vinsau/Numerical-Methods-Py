import sys

def f(x) -> float:
    return (x ** 3) - (4 * x) - 9

def findInterval(a_start, b_start, step):
    MAX_I = 1000
    i = 0
    a = a_start
    b = b_start
    
    while (f(a) * f(b) >= 0) and i < MAX_I:
        a += step
        b += step
        i += 1
    
    if i == MAX_I:
        print("No interval with opposite signs found")
        sys.exit(1)

    return a, b 

def main():
    a = 0.0
    b = 1.0
    step = 0.1
    
    a, b = findInterval(a, b, step)
    
    TOL = 0.00001
    count = 0
    
    while (b - a) >= TOL:  # Fixed condition
        count += 1
        c = (a + b) / 2
        
        if abs(f(c)) < TOL:  # Absolute value check
            break
            
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    
    # Final approximation
    c = (a + b) / 2
    print(f"Approximate root: {c:.6f}")
    print(f"Total Iterations: {count}")

main()