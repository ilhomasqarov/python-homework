import threading
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result_list):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    result_list.extend(primes)

def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    results = []
    range_size = (end - start + 1) // num_threads
    results_lists = [[] for _ in range(num_threads)]

    for i in range(num_threads):
        sub_start = start + i * range_size
        # For last thread, ensure it covers up to 'end'
        sub_end = (start + (i + 1) * range_size - 1) if i != num_threads -1 else end
        t = threading.Thread(target=check_primes, args=(sub_start, sub_end, results_lists[i]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Combine all results
    for r in results_lists:
        results.extend(r)

    results.sort()
    return results

if __name__ == "__main__":
    start_num = 10
    end_num = 100
    print(f"Checking primes between {start_num} and {end_num} using threads...")
    primes = threaded_prime_checker(start_num, end_num, num_threads=4)
    print("Primes found:", primes)
