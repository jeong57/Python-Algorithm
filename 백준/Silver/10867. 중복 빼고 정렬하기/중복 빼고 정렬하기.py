N = int(input())
arr = list(map(int, input().split()))
arr = sorted(list(set(arr)))
print(*arr)