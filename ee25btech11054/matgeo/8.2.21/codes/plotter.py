import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(-8, 8, 400)
y_vals = (2.0 / 25.0) * x_vals**2

plt.figure(figsize=(8, 6))

plt.plot(x_vals, y_vals, label=r'$y = \frac{2}{25}x^2$', color='blue')

plt.scatter([0], [0], color='red', zorder=5)
plt.annotate('Vertex (0,0)', xy=(0, 0), xytext=(0.5, 1))

plt.scatter([5], [2], color='green', zorder=5)
plt.annotate('Point (5,2)', xy=(5, 2), xytext=(2.5, 3))

plt.title('Parabola with Vertex at (0,0)')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.axis('equal')
plt.legend()

plt.show()
