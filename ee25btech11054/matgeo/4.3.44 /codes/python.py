import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

os.makedirs("../figs", exist_ok=True)

A = np.array([5, 1, 6])
B = np.array([3, 4, 1])

direction = B - A
t = -A[0] / direction[0]
C = A + t * direction

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

line_points = np.array([A + s * direction for s in np.linspace(-0.5, t + 0.5, 100)])
ax.plot(line_points[:, 0], line_points[:, 1], line_points[:, 2], 'b-', linewidth=2)

ax.scatter(*A, color='red', s=100, label='A')
ax.scatter(*B, color='blue', s=100, label='B')
ax.scatter(*C, color='green', s=100, label='C')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Line crossing YZ-plane')
ax.legend(loc='upper right')
ax.grid(True)

plt.tight_layout()
plt.savefig('../figs/plot.png', dpi=300, bbox_inches='tight')
plt.show()

print(f"Point C: ({C[0]:.2f}, {C[1]:.2f}, {C[2]:.2f})")