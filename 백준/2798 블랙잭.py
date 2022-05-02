"""
5 21
5 6 7 8 9

"""

N, M = map(int, input().split())
arr = list(map(int, input().split()))

max_value = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            tot = arr[i] + arr[j] + arr[k]
            if max_value < tot <= M:
                max_value = tot
print(max_value)
