import sys

MOD = 998244353


def solve():
    data = list(map(int, sys.stdin.read().strip().split()))
    it = iter(data)
    N = next(it)

    xa = next(it)
    Afix = set(next(it) for _ in range(xa))

    xb = next(it)
    Bfix = set(next(it) for _ in range(xb))

    if Afix & Bfix:
        print(0)
        return

    forced = [0] * (2 * N + 1)
    for v in Afix:
        if 1 <= v <= 2 * N:
            forced[v] = +1
        else:
            print(0)
            return
    for v in Bfix:
        if 1 <= v <= 2 * N:
            forced[v] = -1
        else:
            print(0)
            return

    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(0, 2 * N):
        ndp = [0] * (N + 1)
        for b in range(0, N + 1):
            ways = dp[b]
            if not ways:
                continue
            ups = (i + b) // 2
            downs = i - ups
            f = forced[i + 1]
            if f in (0, +1):
                if ups < N and b + 1 <= N:
                    ndp[b + 1] = (ndp[b + 1] + ways) % MOD
            if f in (0, -1):
                if b > 0 and downs < N:
                    ndp[b - 1] = (ndp[b - 1] + ways) % MOD
        dp = ndp

    print(dp[0] % MOD)


if __name__ == "__main__":
    solve()
