
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")


try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("That's not valid integer.")

try:
    with open("missing_file.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found.")

try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    result = float(a) + float(b)
except ValueError:
    raise TypeError("Both inputs must be numerical.")

try:
    with open("/root/secret.txt", "r") as f:
        print(f.read())
except PermissionError:
    print("Permission denied.")

my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Index out of range.")


try:
    n = input("Enter a number (Press Ctrl+C to interrupt): ")
except KeyboardInterrupt:
    print("\nInput cancelled by user.")

try:
    x = 10 / 0
except ArithmeticError:
    print("Arithmetic error occurred.")

try:
    with open("utf16_encoded_file.txt", encoding='utf-8') as f:
        print(f.read())
except UnicodeDecodeError:
    print("Encoding issue with file.")


try:
    my_list = [1, 2, 3]
    my_list.upper() 
except AttributeError:
    print("Attribute error: method doesn't exist for object.")



with open("sample.txt") as f:
    print(f.read())


n = 3
with open("sample.txt") as f:
    for i in range(n):
        print(f.readline(), end='')


with open("sample.txt", "a") as f:
    f.write("\nNew line added.")
with open("sample.txt") as f:
    print(f.read())


from collections import deque
n = 3
with open("sample.txt") as f:
    last_lines = deque(f, maxlen=n)
print(''.join(last_lines))


with open("sample.txt") as f:
    lines = f.readlines()
print(lines)


with open("sample.txt") as f:
    content = f.read()
print(content)


with open("sample.txt") as f:
    arr = [line.strip() for line in f]
print(arr)

with open("sample.txt") as f:
    words = f.read().split()
    longest = max(words, key=len)
print("Longest word:", longest)


with open("sample.txt") as f:
    line_count = sum(1 for _ in f)
print("Line count:", line_count)


from collections import Counter
with open("sample.txt") as f:
    words = f.read().replace(',', ' ').split()
    word_freq = Counter(words)
print(word_freq)


import os
print("File size:", os.path.getsize("sample.txt"), "bytes")


items = ['apple', 'banana', 'cherry']
with open("fruits.txt", "w") as f:
    f.write("\n".join(items))


with open("sample.txt") as src, open("copy.txt", "w") as dest:
    dest.write(src.read())

with open("file1.txt") as f1, open("file2.txt") as f2:
    for line1, line2 in zip(f1, f2):
       
