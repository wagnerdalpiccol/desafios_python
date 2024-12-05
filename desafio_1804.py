import sys

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, idx, delta):
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & -idx
        return total

n = int(input())
i = list(map(int, input().split()))

fenwick = FenwickTree(n)
for idx, val in enumerate(i, start=1):
    fenwick.update(idx, val)

v = sys.stdin.read().strip().split("\n")
for x in v:
    if not x.strip():
        continue
    a = x.split()
    if a[0] == "a":
        idx = int(a[1])
        delta = -i[idx - 1]
        fenwick.update(idx, delta)
        i[idx - 1] = 0
    elif a[0] == "?":
        print(fenwick.query(int(a[1]) - 1))
