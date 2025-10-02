#include <stdio.h>
#include <math.h>

double dotProduct(double a[], double b[]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

void crossProduct(double a[], double b[], double result[]) {
    result[0] = a[1]*b[2] - a[2]*b[1];
    result[1] = a[2]*b[0] - a[0]*b[2];
    result[2] = a[0]*b[1] - a[1]*b[0];
}

double magnitude(double v[]) {
    return sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2]);
}

int main() {
    double u[3] = {1.0, 0.0, 0.0};
    double v[3] = {0.25, sqrt(15.0)/4.0, 0.0};
    
    printf("Vector u: [%.4f, %.4f, %.4f]\n", u[0], u[1], u[2]);
    printf("Vector v: [%.4f, %.4f, %.4f]\n", v[0], v[1], v[2]);
    
    printf("\nMagnitude of u: %.4f\n", magnitude(u));
    printf("Magnitude of v: %.4f\n", magnitude(v));
    printf("u · v: %.4f\n", dotProduct(u, v));
    
    double u_cross_v[3];
    crossProduct(u, v, u_cross_v);
    double mag_cross = magnitude(u_cross_v);
    
    printf("\nu × v: [%.4f, %.4f, %.4f]\n", u_cross_v[0], u_cross_v[1], u_cross_v[2]);
    printf("|u × v|: %.4f\n", mag_cross);
    
    double alpha = 0.2;
    double beta = 0.2;
    double gamma = sqrt(2.0) / mag_cross;
    
    printf("gamma: %.4f\n", gamma);
    
    double w[3];
    for(int i = 0; i < 3; i++) {
        w[i] = alpha*u[i] + beta*v[i] + gamma*u_cross_v[i];
    }
    
    printf("\nVector w: [%.4f, %.4f, %.4f]\n", w[0], w[1], w[2]);
    printf("u · w: %.4f\n", dotProduct(u, w));
    printf("v · w: %.4f\n", dotProduct(v, w));
    
    double cross_vw[3];
    crossProduct(v, w, cross_vw);
    double volume = fabs(dotProduct(u, cross_vw));
    printf("Volume: %.4f\n", volume);
    
    double result[3];
    for(int i = 0; i < 3; i++) {
        result[i] = 3.0*u[i] + 5.0*v[i];
    }
    
    double result_mag = magnitude(result);
    
    printf("\n3u + 5v: [%.4f, %.4f, %.4f]\n", result[0], result[1], result[2]);
    printf("|3u + 5v|: %.4f\n", result_mag);
    
    return 0;
}
