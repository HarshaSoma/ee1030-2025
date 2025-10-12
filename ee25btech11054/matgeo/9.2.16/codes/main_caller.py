import ctypes
import os

lib_path = os.path.join(os.getcwd(), 'libarea.so')
area_calculator_lib = ctypes.CDLL(lib_path)

area_calculator_lib.calculate_area.argtypes = [ctypes.c_int]
area_calculator_lib.calculate_area.restype = ctypes.c_double

num_intervals = 100000
area = area_calculator_lib.calculate_area(num_intervals)

print(f"Calculating area using the C library...")
print(f"The calculated area is: {area}")
print(f"The exact area is 1/6 ≈ {1/6}")
