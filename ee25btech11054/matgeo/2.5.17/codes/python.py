import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = np.array([1, -7, 7])
b = np.array([3, -2, 2])

perpendicular_vector = np.cross(a, b)
magnitude = np.linalg.norm(perpendicular_vector)

if magnitude > 0:
    unit_vector = perpendicular_vector / magnitude
else:
    unit_vector = np.array([0, 0, 0])

print(f"Vector a: {a}")
print(f"Vector b: {b}")
print(f"Perpendicular Vector (a x b): {perpendicular_vector}")
print(f"Unit Vector (n): {unit_vector}")

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

origin = [0, 0, 0]

ax.quiver(*origin, *a, color='r', label='Vector a', arrow_length_ratio=0.1)
ax.quiver(*origin, *b, color='b', label='Vector b', arrow_length_ratio=0.1)
ax.quiver(*origin, *(unit_vector * 5), color='g', label='Unit Vector n (scaled x5)', arrow_length_ratio=0.2)

max_val = np.max(np.abs(np.concatenate((a, b)))) * 1.2
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Visualization of Vectors')
ax.legend()

ax.view_init(elev=20, azim=30)
plt.grid(True)
plt.show()
