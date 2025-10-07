def main():
    n, m = map(int, input().split())
    arr = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        arr[u].append(v)

    for i in range(1, n + 1):
        print(i, end="")
        for it in arr[i]:
            print(it, end="")
        print()

if __name__ == "__main__":
    main()
