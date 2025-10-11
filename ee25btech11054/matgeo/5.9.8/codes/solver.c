#include <math.h>

int solve_system(double A[2][2], double b[2], double result[2]) {
    double det = A[0][0] * A[1][1] - A[0][1] * A[1][0];

    if (fabs(det) < 1e-9) {
        return 0;
    }

    double inv_det = 1.0 / det;
    double A_inv[2][2];
    A_inv[0][0] =  A[1][1] * inv_det;
    A_inv[0][1] = -A[0][1] * inv_det;
    A_inv[1][0] = -A[1][0] * inv_det;
    A_inv[1][1] =  A[0][0] * inv_det;

    result[0] = A_inv[0][0] * b[0] + A_inv[0][1] * b[1];
    result[1] = A_inv[1][0] * b[0] + A_inv[1][1] * b[1];
    
    return 1;
}

