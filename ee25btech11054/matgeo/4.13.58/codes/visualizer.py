import ctypes
import os
import numpy as np
import matplotlib.pyplot as plt

def main():
    lib_name = "./libsolver.so"
    if os.name == 'nt':
        lib_name = "./libsolver.dll"
    elif os.uname().sysname == 'Darwin':
        lib_name = "./libsolver.dylib"

    try:
        c_lib = ctypes.CDLL(lib_name)
    except OSError:
        print(f"Error: Could not load the shared library '{lib_name}'.")
        print("Please compile the C code first.")
        return

    c_lib.find_intersections.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double)]
    c_lib.find_intersections.restype = ctypes.c_int

    fig, ax = plt.subplots(figsize=(10, 8))
    
    x = np.linspace(-5, 7, 400)
    y = np.linspace(-6, 6, 400)
    X, Y = np.meshgrid(x, y)

    curve_eq = 3*X**2 - Y**2 - 2*X + 4*Y

    ax.contour(X, Y, curve_eq, levels=[0], colors='blue')

    fixed_point = (1, -2)
    ax.plot(0, 0, 'ko', markersize=8, label='Origin (0, 0)')
    ax.plot(fixed_point[0], fixed_point[1], 'r*', markersize=15, label=f'Fixed Point {fixed_point}')

    # --- MODIFIED PART ---
    # Instead of 10 chords, we will plot only 3 for a simpler image.
    m_values = [-1.5, 0.2, 1.0]
    chord_colors = ['green', 'purple', 'orange']
    
    for i, m in enumerate(m_values):
        l = 1 + 2 * m
        out_points = (ctypes.c_double * 4)()
        result = c_lib.find_intersections(l, m, out_points)
        
        if result == 0:
            p1 = (out_points[0], out_points[1])
            p2 = (out_points[2], out_points[3])

            color = chord_colors[i]
            # Plot the chord itself
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], '-o', color=color, alpha=0.9, label=f'Chord {i+1}')
            
            # Plot lines from origin showing the right angle
            ax.plot([0, p1[0]], [0, p1[1]], '--', color=color, alpha=0.7)
            ax.plot([0, p2[0]], [0, p2[1]], '--', color=color, alpha=0.7)

    ax.set_title("Chords Subtending a Right Angle at the Origin")
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    main()
