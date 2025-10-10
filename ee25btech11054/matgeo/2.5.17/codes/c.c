#include <stdio.h>
#include <math.h>

typedef struct {
    double x, y, z;
} Vector3D;

Vector3D cross_product(Vector3D a, Vector3D b) {
    Vector3D result;
    result.x = a.y * b.z - a.z * b.y;
    result.y = a.z * b.x - a.x * b.z;
    result.z = a.x * b.y - a.y * b.x;
    return result;
}

double magnitude(Vector3D v) {
    return sqrt(v.x * v.x + v.y * v.y + v.z * v.z);
}

void print_vector(const char* name, Vector3D v) {
    printf("%s = (%f, %f, %f)\n", name, v.x, v.y, v.z);
}

int main() {
    Vector3D a = {1.0, -7.0, 7.0};
    Vector3D b = {3.0, -2.0, 2.0};

    printf("Given Vectors:\n");
    print_vector("a", a);
    print_vector("b", b);

    Vector3D perpendicular_vector = cross_product(a, b);
    printf("\nPerpendicular Vector (a x b):\n");
    print_vector("p", perpendicular_vector);

    double mag = magnitude(perpendicular_vector);
    printf("\nMagnitude of perpendicular vector: %f\n", mag);

    Vector3D unit_vector = {0, 0, 0};
    if (mag > 0) {
        unit_vector.x = perpendicular_vector.x / mag;
        unit_vector.y = perpendicular_vector.y / mag;
        unit_vector.z = perpendicular_vector.z / mag;
    }

    printf("\nResultant Unit Vector:\n");
    print_vector("n", unit_vector);

    return 0;
}


