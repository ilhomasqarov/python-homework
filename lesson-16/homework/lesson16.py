import numpy as np

lst = [12.23, 13.32, 100, 36.32]
arr = np.array(lst)
print("Original List:", lst)
print("One-dimensional NumPy array:", arr)

arr = np.arange(2, 11).reshape(3, 3)
print(arr)

arr = np.zeros(10)
print("Original vector:", arr)
arr[6] = 11
print("Updated vector:", arr)

arr = np.arange(12, 38)
print(arr)

arr = np.array([1, 2, 3, 4])
float_arr = arr.astype(float)
print("Original array:", arr)
print("Float array:", float_arr)


celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = celsius * 9 / 5 + 32

print("Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)


fahrenheit = np.array([0., 12., 45.21, 34., 99.91, 32.])
celsius = (fahrenheit - 32) * 5 / 9
print("Converted to Celsius:", celsius)


arr = np.array([10, 20, 30])
new_arr = np.append(arr, [40, 50, 60, 70, 80, 90])
print("Original array:", arr)
print("After append:", new_arr)

arr = np.random.rand(10)  # 10 random floats in [0, 1)
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))

arr = np.random.rand(10, 10)
print("Array:\n", arr)
print("Minimum value:", np.min(arr))
print("Maximum value:", np.max(arr))

