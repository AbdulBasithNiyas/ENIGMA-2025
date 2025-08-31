import math

n = int(input().strip())
orig = n
factors = []

# factor out 2
count = 0
while n % 2 == 0:
    n //= 2
    count += 1
if count > 0:
    factors.append((2, count))

# factor odd numbers
p = 3
limit = int(math.isqrt(n)) + 1
while p <= limit and n > 1:
    if n % p == 0:
        count = 0
        while n % p == 0:
            n //= p
            count += 1
        factors.append((p, count))
        limit = int(math.isqrt(n)) + 1
    p += 2

# if remainder is prime
if n > 1:
    factors.append((n, 1))

# format output
output_parts = []
for p, e in factors:
    if e == 1:
        output_parts.append(str(p))
    else:
        output_parts.append(f"{p}^{e}")

print(" * ".join(output_parts))
