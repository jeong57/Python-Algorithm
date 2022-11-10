A, B = map(int, input().split())

arr = [0] * 1000
cnt = 1
tot = 1
while tot < 1000:
    for i in range(cnt):
        arr[tot-1] = cnt
        tot += 1
        if tot > 1000:
            break
    cnt += 1
print(sum(arr[A-1:B]))