def count_distinct(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0

    mod = 2**61 - 1
    base = 257

    seen = set()

    for length in range(1, n + 1):
        power = 1
        for _ in range(length):
            power = (power * base) % mod

        current_hash = 0
        for i in range(length):
            current_hash = (current_hash * base + ord(s[i])) % mod

        seen.add(current_hash)

        for i in range(length, n):
            current_hash = (current_hash * base + ord(s[i]) - ord(s[i - length]) * power) % mod
            if current_hash < 0:
                current_hash += mod
            seen.add(current_hash)

    return len(seen)


if __name__ == "__main__":
    print(count_distinct(input()))
