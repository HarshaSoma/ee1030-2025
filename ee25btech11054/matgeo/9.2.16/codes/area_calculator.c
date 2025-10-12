#include <math.h>

double calculate_area(int n) {
    double a = 0.0;
    double b = 1.0;
    double h = (b - a) / n;
    double sum = 0.0;
    
    for (int i = 1; i < n; i++) {
        double x_i = a + i * h;
        sum += sqrt(x_i) - x_i;
    }
    
    double area = h * sum;
    return area;
}
