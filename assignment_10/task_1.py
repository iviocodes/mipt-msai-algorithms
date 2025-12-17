if __name__ == "__main__":
    n = int(input())
    logins = set()
    for _ in range(n):
        s = input()
        logins.add(s)
    print(len(logins))
