iimport ctypes
import os

lib_path = os.path.join(os.getcwd(), 'libparabola.so')
parabola_lib = ctypes.CDLL(lib_path)

parabola_lib.calculate_y.argtypes = [ctypes.c_double]
parabola_lib.calculate_y.restype = ctypes.c_double

x_test = 5.0
y_result = parabola_lib.calculate_y(x_test)

print(f"Calling C function with x = {x_test}")
print(f"The calculated y value is: {y_result}")
