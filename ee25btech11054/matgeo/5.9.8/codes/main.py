import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./libsolver.so")

lib.solve_system.argtypes = [
    (ctypes.c_double * 2) * 2,
    ctypes.c_double * 2,
    ctypes.c_double * 2
]
lib.solve_system.restype = ctypes.c_int

A = np.array([[1, -3], [1, -2]], dtype=np.double)
b = np.array([0, 15], dtype=np.double)

A_c = ((ctypes.c_double*2)*2)(*map(tuple, A))
b_c = (ctypes.c_double*2)(*b)
solution_c = (ctypes.c_double*2)()

status = lib.solve_system(A_c, b_c, solution_c)

if status:
    fathers_age = solution_c[0]
    sum_childrens_ages = solution_c[1]
    
    print("Solution from C library:")
    print(f"Father's present age: {fathers_age:.0f}")
    print(f"Sum of children's present ages: {sum_childrens_ages:.0f}")
    
    F_vals = np.linspace(0, 50, 100)
    S1 = F_vals / 3.0
    S2 = (F_vals - 15.0) / 2.0
    
    plt.figure(figsize=(8, 6))
    plt.plot(F_vals, S1, color='blue')
    plt.plot(F_vals, S2, color='green')
    
    plt.plot(fathers_age, sum_childrens_ages, 'ro', markersize=10)
    
    # Add text annotations directly to the plot
    plt.text(30, 11, 'F = 3S', color='blue', fontsize=12)
    plt.text(35, 9, 'F - 2S = 15', color='green', fontsize=12)
    plt.text(fathers_age - 1, sum_childrens_ages + 1, f'Solution ({fathers_age:.0f}, {sum_childrens_ages:.0f})', 
             color='red', fontsize=12, ha='right')
    
    plt.xlabel("Father's Age (F)")
    plt.ylabel("Sum of Children's Ages (S)")
    plt.title("Graphical Solution with Annotations")
    plt.grid(True)
    plt.xlim(0, 50)
    plt.ylim(0, 20)
    plt.show()

else:
    print("Could not solve the system.")


