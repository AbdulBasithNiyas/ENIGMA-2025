import sys
import bisect
import math
input = sys.stdin.readline


class RangeAddRangeSum:
    def __init__(self, n):
        self.n = n
        self.bit1 = [0]*(n+1)
        self.bit2 = [0]*(n+1)

    def _add(self, bit, i, v):
        while i <= self.n:
            bit[i] += v
            i += i & -i

    def add_range(self, l, r, v):
        self._add(self.bit1, l, v)
        self._add(self.bit1, r+1, -v)
        self._add(self.bit2, l, v*(l-1))
        self._add(self.bit2, r+1, -v*r)

    def _prefix(self, i):
        s1 = s2 = 0
        j = i
        while j > 0:
            s1 += self.bit1[j]
            j -= j & -j
        j = i
        while j > 0:
            s2 += self.bit2[j]
            j -= j & -j
        return s1*i - s2

    def range_sum(self, l, r):
        if l > r:
            return 0
        return self._prefix(r) - self._prefix(l-1)


N, Q = map(int, input().split())
P = [0] + list(map(int, input().split()))
Pinv = [0]*(N+1)
for pos in range(1, N+1):
    Pinv[P[pos]] = pos

B = int(math.sqrt(N)) + 1

index_blocks = [[] for _ in range((N + B - 1)//B)]
for x in range(1, N+1):
    index_blocks[(x-1)//B].append(Pinv[x])
for g in index_blocks:
    g.sort()

pos_blocks = [[] for _ in range((N + B - 1)//B)]
for pos in range(1, N+1):
    pos_blocks[(pos-1)//B].append(P[pos])
for g in pos_blocks:
    g.sort()

tree_index = RangeAddRangeSum(N)
tree_pos = RangeAddRangeSum(N)

index_block_sum = [0]*len(index_blocks)
pos_block_sum = [0]*len(pos_blocks)

out_lines = []

for _ in range(Q):
    parts = input().split()
    t = int(parts[0])

    if t == 0:
        l, r, c = map(int, parts[1:])
        tree_index.add_range(l, r, c)
        for bid, g in enumerate(pos_blocks):
            if not g:
                continue
            lo = bisect.bisect_left(g, l)
            hi = bisect.bisect_right(g, r)
            if lo < hi:
                pos_block_sum[bid] += (hi - lo) * c

    elif t == 1:
        l, r, c = map(int, parts[1:])
        tree_pos.add_range(l, r, c)
        for bid, g in enumerate(index_blocks):
            if not g:
                continue
            lo = bisect.bisect_left(g, l)
            hi = bisect.bisect_right(g, r)
            if lo < hi:
                index_block_sum[bid] += (hi - lo) * c

    elif t == 2:
        l, r = map(int, parts[1:])
        ans = tree_index.range_sum(l, r)
        L, R = (l-1)//B, (r-1)//B
        if L == R:
            for x in range(l, r+1):
                ans += tree_pos.range_sum(Pinv[x], Pinv[x])
        else:
            endL = (L+1)*B
            for x in range(l, endL+1):
                ans += tree_pos.range_sum(Pinv[x], Pinv[x])
            for b in range(L+1, R):
                ans += index_block_sum[b]
            startR = R*B + 1
            for x in range(startR, r+1):
                ans += tree_pos.range_sum(Pinv[x], Pinv[x])
        out_lines.append(str(ans))

    elif t == 3:
        l, r = map(int, parts[1:])
        ans = tree_pos.range_sum(l, r)
        L, R = (l-1)//B, (r-1)//B
        if L == R:
            for pos in range(l, r+1):
                ans += tree_index.range_sum(P[pos], P[pos])
        else:
            endL = (L+1)*B
            for pos in range(l, endL+1):
                ans += tree_index.range_sum(P[pos], P[pos])
            for b in range(L+1, R):
                ans += pos_block_sum[b]
            startR = R*B + 1
            for pos in range(startR, r+1):
                ans += tree_index.range_sum(P[pos], P[pos])
        out_lines.append(str(ans))

print("\n".join(out_lines))
