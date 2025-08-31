import sys

tokens = sys.stdin.read().split()
it = iter(tokens)

L = int(next(it))
count_A = int(next(it))
count_B = int(next(it))

limit = 2 * L

vertical = set()
horizontal = set()


def add_cut(dir_token, pos_token):
    d = dir_token.upper()
    try:
        p = int(pos_token)
    except:
        return
    if not (0 < p < limit):
        return
    if d in ("U", "D"):
        vertical.add(p)
    elif d in ("R", "L"):
        horizontal.add(p)


for x in range(count_A):
    add_cut(next(it), next(it))

for y in range(count_B):
    add_cut(next(it), next(it))

V = len(vertical)
H = len(horizontal)
print((V + 1) * (H + 1))
