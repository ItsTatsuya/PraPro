"""
Create a 1000 x 1000 random numpy array
Measure how long the creation takes
Convert the array into bytes
Recreate the array from the bytes

References:
time package
numpy package
np.frombuffer
"""

import numpy as np
import time

def create_array():
    start = time.time()
    arr = np.random.rand(1000, 1000)
    end = time.time()
    print(f"Time taken to create array: {end - start} secs")
    return arr

def convert_to_bytes(arr):
    return arr.tobytes()

def recreate_array(arr_bytes):
    return np.frombuffer(arr_bytes).reshape(1000, 1000)

def main():
    arr = create_array()
    arr_bytes = convert_to_bytes(arr)
    recreated_arr = recreate_array(arr_bytes)
    print(f"Original array:\n{arr}\n")
    print(f"Array in bytes:\n{arr_bytes}\n")
    print(f"Recreated array:\n{recreated_arr}")
    
if __name__ == "__main__":
    main()