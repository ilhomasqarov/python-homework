def check_weird(n):
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")

  def even_numbers_if_else(a, b):
    start = a if a % 2 == 0 else a + 1
    end = b
    if start > end:
        print([])
    else:
        result = list(range(start, end + 1, 2))
        print(result)


def even_numbers_no_if(a, b):
    start = a + (a % 2)       # if a is odd, move to next even
    result = list(range(start, b + 1, 2)) * (start <= b)
    print(result)
