import sys
input = sys.stdin.readline


def perm(n, k):
    global result
    if n == k:
        ssum = 0
        for i in range(N-1):
            ssum += abs(arr[i]-arr[i+1])
        result = max(result, ssum)
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k+1)
            arr[i], arr[k] = arr[k], arr[i]


N = int(input())
arr = list(map(int, input().split()))
result = 0
perm(N, 0)
print(result)