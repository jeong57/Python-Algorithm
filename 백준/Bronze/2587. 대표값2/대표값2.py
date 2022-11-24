arr = list(int(input()) for _ in range(5))
print(int(sum(arr) / 5))
arr.sort()
print(arr[2])