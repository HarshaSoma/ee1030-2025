#include <math.h>

double integrand(double y) {
    if (16.0 - y * y < 0) {
        return 0.0;
    }
    return sqrt(16.0 - y * y) - (y * y / 6.0);
}

double calculate_common_area(double a, double b, int n) {
    double h = (b - a) / n;
    double sum = integrand(a) + integrand(b);

    for (int i = 1; i < n; i += 2) {
        sum += 4 * integrand(a + i * h);
    }

    for (int i = 2; i < n; i += 2) {
        sum += 2 * integrand(a + i * h);
    }

    return (h / 3.0) * sum;
}


