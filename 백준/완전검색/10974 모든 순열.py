def perm(n, k):
    if n == k:
        print(*p)
    else:
        for i in range(n):
            if not used[i]:
                used[i] = 1
                p[k] = lst[i]
                perm(n, k+1)
                used[i] = 0


N = int(input())
lst = list(range(1, N+1))
used = [0] * N
p = [0] * N
perm(N, 0)
