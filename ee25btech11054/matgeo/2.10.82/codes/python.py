import numpy as np
import matplotlib.pyplot as plt

u = np.array([1, 0, 0])
v = np.array([1/4, np.sqrt(15)/4, 0])
w = np.array([1, 3/np.sqrt(15), 4*np.sqrt(2)/np.sqrt(15)])

print("--- Verification of Given Conditions ---")

norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)
print(f"Magnitude of u: {norm_u:.4f}")
print(f"Is u a unit vector? {np.isclose(norm_u, 1)}")
print(f"Magnitude of v: {norm_v:.4f}")
print(f"Is v a unit vector? {np.isclose(norm_v, 1)}\n")

dot_uv = np.dot(u, v)
dot_uw = np.dot(u, w)
dot_vw = np.dot(v, w)
print(f"Dot product u · v: {dot_uv:.4f} (Expected: 0.25)")
print(f"Dot product u · w: {dot_uw:.4f} (Expected: 1.00)")
print(f"Dot product v · w: {dot_vw:.4f} (Expected: 1.00)\n")

matrix = np.array([u, v, w])
volume = np.abs(np.linalg.det(matrix))
expected_volume = np.sqrt(2)
print(f"Volume of parallelepiped: {volume:.4f}")
print(f"Expected volume (√2):    {expected_volume:.4f}")
print(f"Is volume correct? {np.isclose(volume, expected_volume)}\n")

print("--- Final Answer Computation ---")
resultant_vector = 3 * u + 5 * v
magnitude_resultant = np.linalg.norm(resultant_vector)
analytical_answer = np.sqrt(83/2)

print(f"Resultant vector (3u + 5v): {resultant_vector}")
print(f"Value of |3u + 5v| (numerical): {magnitude_resultant:.4f}")
print(f"Value of |3u + 5v| (analytical, √83/2): {analytical_answer:.4f}\n")

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(projection='3d')

origin = np.array([0, 0, 0])

ax.quiver(*origin, *u, color='r', label='u')
ax.quiver(*origin, *v, color='g', label='v')
ax.quiver(*origin, *w, color='b', label='w')
ax.quiver(*origin, *resultant_vector, color='m', label='3u + 5v', linewidth=2, arrow_length_ratio=0.1)

p0 = origin
p1 = u
p2 = v
p3 = w
p4 = u + v
p5 = u + w
p6 = v + w
p7 = u + v + w

edges = [
    (p0, p1), (p0, p2), (p0, p3), (p1, p4), (p1, p5),
    (p2, p4), (p2, p6), (p3, p5), (p3, p6), (p4, p7),
    (p5, p7), (p6, p7)
]

for start, end in edges:
    ax.plot(*zip(start, end), color='k', linestyle=':')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Visualization of Parallelepiped and Vectors')

all_points = np.array([p0, p1, p2, p3, p4, p5, p6, p7, resultant_vector])
max_val = np.max(all_points)
min_val = np.min(all_points)
ax.set_xlim([min_val, max_val])
ax.set_ylim([min_val, max_val])
ax.set_zlim([min_val, max_val])
ax.legend()
ax.grid(True)
ax.set_aspect('equal', adjustable='box')

plt.show()
