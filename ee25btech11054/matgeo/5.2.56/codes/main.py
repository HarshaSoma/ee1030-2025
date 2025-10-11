import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./libequationsolve.so")

# Define argument/return types (no changes needed here)
lib.solve_system.argtypes = [((ctypes.c_double*2)*2), (ctypes.c_double*2), (ctypes.c_double*2)]
lib.solve_system.restype = ctypes.c_int

# Define the new system: 5u + v = 2, 6u - 3v = 1
# where u = 1/(x-1) and v = 1/(y-2)
A = np.array([[5, 1], [6, -3]], dtype=np.double)
b = np.array([2, 1], dtype=np.double)

# Convert to C types
A_c = ((ctypes.c_double*2)*2)(*[((ctypes.c_double*2)(*row)) for row in A])
b_c = (ctypes.c_double*2)(*b)
result = (ctypes.c_double*2)()

# Solve for u and v using the C function
success = lib.solve_system(A_c, b_c, result)

if success:
    u, v = result[0], result[1]
    
    # Reverse the substitution to find x and y
    x = 1.0 / u + 1
    y = 1.0 / v + 2
    
    print(f"Solved for intermediate variables: u = {u:.6f}, v = {v:.6f}")
    print(f"Final Solution: x = {x:.6f}, y = {y:.6f}")
    
    # Verify the solution in Python
    eq1 = 5/(x-1) + 1/(y-2)
    eq2 = 6/(x-1) - 3/(y-2)
    print(f"\nVerification: 5/(x-1) + 1/(y-2) = {eq1:.6f} (should be 2)")
    print(f"Verification: 6/(x-1) - 3/(y-2) = {eq2:.6f} (should be 1)")
    
    # Plot the original curves
    xx = np.linspace(0, 8, 1000)
    # Avoid asymptotes at x=1, x=3.5, and y=2
    xx = xx[np.abs(xx-1) > 0.01] 
    xx = xx[np.abs(2 - 5/(xx-1)) > 0.01]

    # Calculate y values for both equations
    # From 5/(x-1) + 1/(y-2) = 2  => y = 2 + 1 / (2 - 5/(x-1))
    y1 = 2 + 1 / (2 - 5/(xx-1))
    # From 6/(x-1) - 3/(y-2) = 1  => y = 2 + 3 / (6/(x-1) - 1)
    y2 = 2 + 3 / (6/(xx-1) - 1)
    
    plt.figure(figsize=(8, 8))
    plt.plot(xx, y1, 'b-', label='5/(x-1) + 1/(y-2) = 2')
    plt.plot(xx, y2, 'g-', label='6/(x-1) - 3/(y-2) = 1')
    
    # Plot the solution point
    plt.plot(x, y, 'ro', markersize=10, label=f'Solution ({x:.1f}, {y:.1f})')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('System of Equations Solution')
    plt.legend()
    plt.grid(True)
    plt.xlim(0, 8)
    plt.ylim(0, 8)
    
    plt.show()
