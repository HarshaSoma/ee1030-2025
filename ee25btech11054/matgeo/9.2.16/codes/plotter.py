import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1.2, 500)
y1 = np.sqrt(x)
y2 = x

fill_x = np.linspace(0, 1, 100)
fill_y1 = np.sqrt(fill_x)
fill_y2 = fill_x

area = np.trapz(fill_y1 - fill_y2, fill_x)

plt.figure(figsize=(8, 6))

plt.plot(x, y1, label=r'$y = \sqrt{x}$', color='blue')
plt.plot(x, y2, label=r'$y = x$', color='red')

plt.fill_between(fill_x, fill_y1, fill_y2, color='lightgray', alpha=0.6, label=f'Area ≈ {area:.4f}')

plt.title('Area Between $y = \sqrt{x}$ and $y = x$')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.xlim(0, 1.2)
plt.ylim(0, 1.2)

plt.show()
