def pascal(n):
    for i in range(n):
        arr[i][0] = arr[i][i] = 1
        for i in range(n):
            if i > 1:
                for j in range(1, N-1):
                    arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
    return arr


T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}')
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    result = pascal(N)
    for i in range(N):
        print(*pascal(N)[i][:i+1])