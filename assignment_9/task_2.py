class RSQFenwick:
    def __init__(self, n):
        self.n = n
        self.f = [0] * self.n
    
    def query(self, i):
        res = 0
        while i >= 0:
            res += self.f[i]
            i -= ~i & (i + 1)
        return res
    
    def update(self, i, delta):
        while i < self.n:
            self.f[i] += delta
            i += ~i & (i + 1)
    
    def rsq(self, left, right):
        return self.query(right - 1) - (self.query(left - 1) if left > 0 else 0)



if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    tree = RSQFenwick(n)
    
    for i in range(n):
        if a[i] == 0:
            tree.update(i, 1)
    
    results = []
    
    for _ in range(m):
        parts = input().split()
        cmd = parts[0]
        
        if cmd == '?':
            l, r = int(parts[1]), int(parts[2])
            results.append(str(tree.rsq(l, r)))
        
        elif cmd == '+':
            i, delta = int(parts[1]), int(parts[2])
            
            old_val = a[i]
            new_val = old_val + delta
            a[i] = new_val
            
            was_zero = (old_val == 0)
            is_zero = (new_val == 0)
            
            if was_zero and not is_zero:
                tree.update(i, -1)
            elif not was_zero and is_zero:
                tree.update(i, 1)
    
    print("\n".join(results))
