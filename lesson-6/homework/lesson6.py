def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def digit_sum(k):
    return sum(int(d) for d in str(k))


def powers_of_two(N):
    result = []
    power = 1
    while (2 ** power) <= N:
        result.append(2 ** power)
        power += 1
    print(*result)
