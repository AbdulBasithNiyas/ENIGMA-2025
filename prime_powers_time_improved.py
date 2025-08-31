import random
import math
import sys

sys.setrecursionlimit(1000000)


def is_probable_prime(n):
    if n < 2:
        return False
    # Small primes
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in small_primes:
        if n % p == 0:
            return n == p

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Test with random bases
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def pollards_rho(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    while True:
        x = random.randrange(2, n-1)
        y = x
        c = random.randrange(1, n-1)
        d = 1
        while d == 1:
            x = (pow(x, 2, n) + c) % n
            y = (pow(y, 2, n) + c) % n
            y = (pow(y, 2, n) + c) % n
            d = math.gcd(abs(x - y), n)
            if d == n:
                break
        if d > 1 and d < n:
            return d


def factorize(n, factors):
    if n == 1:
        return
    if is_probable_prime(n):
        factors.append(n)
        return
    d = pollards_rho(n)
    factorize(d, factors)
    factorize(n // d, factors)


N = int(input().strip())

if N == 1:
    print(1)
    sys.exit(0)

factors = []
factorize(N, factors)
factors.sort()

output_parts = []
i = 0
while i < len(factors):
    p = factors[i]
    count = 1
    i += 1
    while i < len(factors) and factors[i] == p:
        count += 1
        i += 1
    if count == 1:
        output_parts.append(str(p))
    else:
        output_parts.append(f"{p}^{count}")

print(" * ".join(output_parts))
