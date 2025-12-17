from math import ceil, log2


class RMQSegmentTree:
    INF = float("inf")

    def __init__(self, a):
        self.N = 2 ** int(ceil(log2(len(a))))
        self.s = [None] * (2 * self.N - 1)
        arr = list(a) + [self.INF] * (self.N - len(a))
        for i in range(self.N):
            self.s[self.N - 1 + i] = arr[i]
        for i in range(self.N - 2, -1, -1):
            self.refresh_s(i)

    def refresh_s(self, i):
        self.s[i] = min(self.s[2 * i + 1], self.s[2 * i + 2])

    def rmq_i(self, l, r, i, li, ri):
        if r <= li or ri <= l:
            return self.INF
        if l <= li and ri <= r:
            return self.s[i]
        middle = li + (ri - li) // 2
        left = self.rmq_i(l, r, 2 * i + 1, li, middle)
        right = self.rmq_i(l, r, 2 * i + 2, middle, ri)
        return min(left, right)

    def update(self, i, v):
        idx = i + self.N - 1
        self.s[idx] = v
        while idx > 0:
            idx = (idx - 1) // 2
            self.refresh_s(idx)

    def rmq(self, l, r):
        return self.rmq_i(l, r, 0, 0, self.N)


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    st = RMQSegmentTree(arr)
    out = []
    for _ in range(m):
        parts = input().split()
        if parts[0] == "?":
            l = int(parts[1])
            r = int(parts[2])
            out.append(str(st.rmq(l, r)))
        else:
            i = int(parts[1])
            v = int(parts[2])
            st.update(i, v)
    print("\n".join(out))
