M = int(input())
N = int(input())

result = []
for num in range(M, N+1):
    check = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                check = 1
                break
        if check == 0:
            result.append(num)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))