def prefix_function(s):
    d = [0] * (len(s) + 1)
    for i in range(2, len(d)):
        d[i] = d[i - 1]
        while s[i - 1] != s[d[i]] and d[i] > 0:
            d[i] = d[d[i]]
        if s[i - 1] == s[d[i]]:
            d[i] += 1
    return d


def find_substrings(s, p):
    substrings = []
    d = prefix_function(p + "$" + s)
    for i in range(len(p) + 1, len(d)):
        if d[i] == len(p):
            substrings.append(i - 2 * len(p) - 1)
    return substrings


def kmp(s1, s2):
    if len(s1) == len(s2):
        text = s1 + s1
        positions = find_substrings(text, s2)

        if not positions:
            return -1
        else:
            n = len(s1)
            min_k = min((n - pos) % n for pos in positions)
            return min_k
    else:
        return -1


if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(kmp(s1, s2))
