import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

u = np.array([1.0, 0.0, 0.0])
v = np.array([0.25, np.sqrt(15)/4, 0.0])

print("Vector u:", u)
print("Vector v:", v)
print("\nMagnitude of u:", np.linalg.norm(u))
print("Magnitude of v:", np.linalg.norm(v))
print("u · v:", np.dot(u, v))

alpha = 0.2
beta = 0.2
u_cross_v = np.cross(u, v)
mag_cross = np.linalg.norm(u_cross_v)
gamma = np.sqrt(2) / mag_cross

w = alpha*u + beta*v + gamma*u_cross_v

print("\nVector w:", w)
print("u · w:", np.dot(u, w))
print("v · w:", np.dot(v, w))

volume = np.abs(np.dot(u, np.cross(v, w)))
print("Volume:", volume)

result_vec = 3*u + 5*v
result_mag = np.linalg.norm(result_vec)

print("\n3u + 5v:", result_vec)
print("|3u + 5v|:", result_mag)

fig = plt.figure(figsize=(14, 10))

ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax1.quiver(0, 0, 0, u[0], u[1], u[2], color='r', arrow_length_ratio=0.15, linewidth=3, label='u')
ax1.quiver(0, 0, 0, v[0], v[1], v[2], color='g', arrow_length_ratio=0.15, linewidth=3, label='v')
ax1.quiver(0, 0, 0, w[0], w[1], w[2], color='b', arrow_length_ratio=0.15, linewidth=3, label='w')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Vectors u, v, w')
ax1.legend()
ax1.grid(True)

ax2 = fig.add_subplot(2, 2, 2, projection='3d')
vertices = np.array([[0, 0, 0], u, v, w, u+v, u+w, v+w, u+v+w])
faces = [[vertices[0], vertices[1], vertices[4], vertices[2]],
         [vertices[0], vertices[1], vertices[5], vertices[3]],
         [vertices[0], vertices[2], vertices[6], vertices[3]],
         [vertices[7], vertices[4], vertices[1], vertices[5]],
         [vertices[7], vertices[4], vertices[2], vertices[6]],
         [vertices[7], vertices[5], vertices[3], vertices[6]]]
poly = Poly3DCollection(faces, alpha=0.25, facecolor='cyan', edgecolor='k', linewidth=1.5)
ax2.add_collection3d(poly)
ax2.quiver(0, 0, 0, u[0], u[1], u[2], color='r', arrow_length_ratio=0.15, linewidth=2.5)
ax2.quiver(0, 0, 0, v[0], v[1], v[2], color='g', arrow_length_ratio=0.15, linewidth=2.5)
ax2.quiver(0, 0, 0, w[0], w[1], w[2], color='b', arrow_length_ratio=0.15, linewidth=2.5)
max_range = 1.5
ax2.set_xlim([-0.2, max_range])
ax2.set_ylim([-0.2, max_range])
ax2.set_zlim([-0.2, max_range])
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title(f'Parallelepiped (Volume={volume:.4f})')
ax2.grid(True)

ax3 = fig.add_subplot(2, 2, 3, projection='3d')
ax3.quiver(0, 0, 0, 3*u[0], 3*u[1], 3*u[2], color='darkred', arrow_length_ratio=0.1, linewidth=2, label='3u')
ax3.quiver(0, 0, 0, 5*v[0], 5*v[1], 5*v[2], color='darkgreen', arrow_length_ratio=0.1, linewidth=2, label='5v')
ax3.quiver(0, 0, 0, result_vec[0], result_vec[1], result_vec[2], color='purple', arrow_length_ratio=0.1, linewidth=3, label='3u+5v')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')
ax3.set_title(f'|3u+5v| = {result_mag:.4f}')
ax3.legend()
ax3.grid(True)

ax4 = fig.add_subplot(2, 2, 4, projection='3d')
ax4.quiver(0, 0, 0, u[0], u[1], u[2], color='r', arrow_length_ratio=0.15, linewidth=2.5, label='u')
ax4.quiver(0, 0, 0, v[0], v[1], v[2], color='g', arrow_length_ratio=0.15, linewidth=2.5, label='v')
ax4.quiver(0, 0, 0, w[0], w[1], w[2], color='b', arrow_length_ratio=0.15, linewidth=2.5, label='w')
ax4.quiver(0, 0, 0, result_vec[0], result_vec[1], result_vec[2], color='purple', arrow_length_ratio=0.1, linewidth=3, label='3u+5v')
ax4.quiver(0, 0, 0, u_cross_v[0], u_cross_v[1], u_cross_v[2], color='orange', arrow_length_ratio=0.15, linewidth=2, label='u×v')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')
ax4.set_title('All Vectors')
ax4.legend()
ax4.grid(True)

plt.tight_layout()
plt.savefig('vector_3d.png', dpi=200)
plt.show()

print("\nPlot saved as 'vector_3d.png'")
