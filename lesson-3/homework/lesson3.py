fruits = ["apple", "banana", "cherry", "orange", "grape"]
print(" Third fruit:", fruits[2])

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated = list1 + list2
print(" Concatenated list:", concatenated)

numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
extracted = [first, middle, last]
print(" Extracted elements:", extracted)

favorite_movies = ["Inception", "Interstellar", "Matrix", "Gladiator", "Avengers"]
movies_tuple = tuple(favorite_movies)
print("Movies tuple:", movies_tuple)

cities = ["London", "Berlin", "Tokyo", "Paris", "New York"]
is_paris = "Paris" in cities
print(" Is 'Paris' in list?:", is_paris)

nums = [1, 2, 3]
duplicated = nums * 2
print(" Duplicated list:", duplicated)

numbers = [10, 20, 30, 40, 50]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(" Swapped list:", numbers)

num_tuple = tuple(range(1, 11))
slice_ = num_tuple[3:8]
print(" Tuple slice (index 3 to 7):", slice_)

colors = ["blue", "red", "green", "blue", "yellow", "blue"]
blue_count = colors.count("blue")
print(" Count of 'blue':", blue_count)

animals = ("cat", "dog", "lion", "tiger", "elephant")
lion_index = animals.index("lion")
print(" Index of 'lion':", lion_index)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged = tuple1 + tuple2
print(" Merged tuple:", merged)

list_example = [1, 2, 3, 4, 5]
tuple_example = (6, 7, 8, 9)
print(Length of list:", len(list_example))
print("  Length of tuple:", len(tuple_example))

number_tuple = (1, 3, 5, 7, 9)
converted_list = list(number_tuple)
print(" Converted list:", converted_list)

num_data = (100, 20, 35, 99, 2, 88)
print("Max:", max(num_data))
print("   Min:", min(num_data))

words = ("python", "code", "logic", "data")
reversed_tuple = words[::-1]
print(" Reversed tuple:", reversed_tuple)
