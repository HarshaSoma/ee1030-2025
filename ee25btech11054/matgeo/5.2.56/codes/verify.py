import numpy as np

# Analytical solution
x = 4.0
y = 5.0

print(f"Analytical Solution: x = {x:.6f}, y = {y:.6f}")

# Verify by substituting into original equations
eq1 = 5/(x-1) + 1/(y-2)
eq2 = 6/(x-1) - 3/(y-2)

print(f"Equation 1 result: {eq1:.6f} (Target: 2)")
print(f"Equation 2 result: {eq2:.6f} (Target: 1)")

# Alternative verification using matrix method in NumPy
A = np.array([[5, 1], [6, -3]])
b = np.array([2, 1])

# Solve for u, v where u = 1/(x-1), v = 1/(y-2)
uv = np.linalg.solve(A, b)
u, v = uv[0], uv[1]

# Calculate x and y from u and v
x_calc = 1/u + 1
y_calc = 1/v + 2

print(f"\nMatrix method from NumPy:")
print(f"u = 1/(x-1) = {u:.6f}, v = 1/(y-2) = {v:.6f}")
print(f"x = {x_calc:.6f}, y = {y_calc:.6f}")
print(f"Matches analytical solution: {abs(x - x_calc) < 1e-9 and abs(y - y_calc) < 1e-9}")
