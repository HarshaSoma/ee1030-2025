import ctypes
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import subprocess

try:
    subprocess.run(
        ['gcc', '-shared', '-fPIC', '-o', 'area_calculator.so', 'area_calculator.c', '-lm'], 
        check=True
    )
    lib = ctypes.CDLL('./area_calculator.so')
    lib.calculate_common_area.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int]
    lib.calculate_common_area.restype = ctypes.c_double
except (subprocess.CalledProcessError, OSError) as e:
    print(f"Error during C library compilation or loading: {e}")
    exit()

y_limit = 2 * np.sqrt(3)
n = 2000

common_area = lib.calculate_common_area(-y_limit, y_limit, n)

total_circle_area = 16 * np.pi
required_area = total_circle_area - common_area
analytical_area = (32 * np.pi - 4 * np.sqrt(3)) / 3

print("="*60)
print("AREA CALCULATION RESULTS")
print("="*60)
print(f"Total Circle Area:          {total_circle_area:.8f}")
print(f"Common Area (Numerical):    {common_area:.8f}")
print(f"Required Area (Numerical):  {required_area:.8f}")
print(f"Required Area (Analytical): {analytical_area:.8f}")
print("="*60)

fig, ax = plt.subplots(figsize=(10, 10))

theta = np.linspace(0, 2 * np.pi, 200)
x_circle = 4 * np.cos(theta)
y_circle = 4 * np.sin(theta)

y_parabola_range = np.linspace(-6, 6, 200)
x_parabola = y_parabola_range**2 / 6

ax.plot(x_circle, y_circle, 'b-', label='Circle: $x^2 + y^2 = 16$')
ax.plot(x_parabola, y_parabola_range, 'orange', label='Parabola: $y^2 = 6x$')

ax.fill(x_circle, y_circle, 'cyan', alpha=0.4, label='Area of Circle Exterior to Parabola')

y_fill = np.linspace(-y_limit, y_limit, 500)
x_circle_fill = np.sqrt(16 - y_fill**2)
x_parabola_fill = y_fill**2 / 6
vertices = list(zip(x_parabola_fill, y_fill)) + list(zip(x_circle_fill, y_fill))[::-1]
polygon = Polygon(vertices, facecolor='white', edgecolor='none')
ax.add_patch(polygon)

x_int, y_int_pos = 2, 2 * np.sqrt(3)
ax.plot([x_int, x_int], [y_int_pos, -y_int_pos], 'ro', markersize=8)

ax.set_title('Area of the Circle Exterior to the Parabola', fontsize=16)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

plt.show()


