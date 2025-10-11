#include <math.h>
#include <stdio.h>

int find_intersections(double l, double m, double* out_points) {
    double a, b, c;

    if (fabs(m) < 1e-9) {
        double x = 1.0 / l;
        a = 1.0;
        b = -4.0;
        c = -(3.0 / (l * l) - 2.0 / l);
        double disc = b * b - 4 * a * c;
        if (disc < 0) return -1;
        out_points[0] = x;
        out_points[2] = x;
        out_points[1] = (-b + sqrt(disc)) / (2 * a);
        out_points[3] = (-b - sqrt(disc)) / (2 * a);
        return 0;
    }

    a = 3 * m * m - l * l;
    b = 2 * l - 2 * m * m - 4 * l * m;
    c = 4 * m - 1;

    double discriminant = b * b - 4 * a * c;

    if (discriminant < 0) {
        return -1;
    }

    double sqrt_disc = sqrt(discriminant);

    double x1 = (-b + sqrt_disc) / (2 * a);
    double x2 = (-b - sqrt_disc) / (2 * a);

    double y1 = (1 - l * x1) / m;
    double y2 = (1 - l * x2) / m;

    out_points[0] = x1;
    out_points[1] = y1;
    out_points[2] = x2;
    out_points[3] = y2;

    return 0;
}
