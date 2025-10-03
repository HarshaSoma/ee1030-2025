#include <stdio.h>
#include <math.h>

int main() {
    float a_mag = 3.0;
    float b_mag = 2.0 * sqrt(3);
    float dot_product = 6.0;
    
    float cos_theta = dot_product / (a_mag * b_mag);
    float sin_theta = sqrt(1 - cos_theta * cos_theta);
    float cross_product_mag = a_mag * b_mag * sin_theta;
    
    printf("Magnitude of a x b = %.2f\n", cross_product_mag);
    
    return 0;
}
