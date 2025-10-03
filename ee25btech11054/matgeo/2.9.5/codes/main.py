import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

magnitude_a = 3
magnitude_b = 2 * np.sqrt(3)
dot_product = 6

cos_theta = dot_product / (magnitude_a * magnitude_b)
theta = np.arccos(cos_theta)

print(f"Angle between vectors: {np.degrees(theta):.2f} degrees")

sin_theta = np.sin(theta)
cross_product_magnitude = magnitude_a * magnitude_b * sin_theta

print(f"|a| = {magnitude_a}")
print(f"|b| = {magnitude_b:.3f}")
print(f"a · b = {dot_product}")
print(f"cos(θ) = {cos_theta:.3f}")
print(f"sin(θ) = {sin_theta:.3f}")
print(f"|a × b| = {cross_product_magnitude:.3f}")
print(f"|a × b| = 6√2 = {6 * np.sqrt(2):.3f}")

a = np.array([3, 0, 0])
b = np.array([2, 2*np.sqrt(2), 0])

print(f"\nVerification:")
print(f"Vector a: {a}")
print(f"Vector b: {b}")
print(f"|a| = {np.linalg.norm(a):.3f}")
print(f"|b| = {np.linalg.norm(b):.3f}")
print(f"a · b = {np.dot(a, b):.3f}")

cross_product = np.cross(a, b)
print(f"a × b = {cross_product}")
print(f"|a × b| = {np.linalg.norm(cross_product):.3f}")

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter([0], [0], [0], color='black', s=100, label='Origin')

ax.quiver(0, 0, 0, a[0], a[1], a[2], color='red', arrow_length_ratio=0.1, linewidth=3, label='Vector a')
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='blue', arrow_length_ratio=0.1, linewidth=3, label='Vector b')
ax.quiver(0, 0, 0, cross_product[0], cross_product[1], cross_product[2], 
          color='green', arrow_length_ratio=0.1, linewidth=3, label='a × b')

ax.text(a[0]/2, a[1]/2, a[2]/2 + 0.2, 'a', fontsize=12, color='red')
ax.text(b[0]/2, b[1]/2 + 0.2, b[2]/2, 'b', fontsize=12, color='blue')
ax.text(cross_product[0]/2, cross_product[1]/2, cross_product[2]/2 + 0.2, 'a×b', fontsize=12, color='green')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Vector Cross Product Visualization\n|a| = 3, |b| = 2√3, a·b = 6')

ax.legend()

max_range = 4
ax.set_xlim([0, max_range])
ax.set_ylim([0, max_range])
ax.set_zlim([0, max_range])

ax.grid(True)

plt.tight_layout()
plt.show()

print(f"\n" + "="*50)
print(f"SOLUTION SUMMARY:")
print(f"="*50)
print(f"Given: |a| = {magnitude_a}, |b| = {magnitude_b:.3f}, a·b = {dot_product}")
print(f"Answer: |a × b| = 6√2 = {cross_product_magnitude:.3f}")
print(f"="*50)
