import sys
sys.stdin = open('input.txt')


def rotation(arr):
    # 빈 리스트(결과)
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = arr[N-1-j][i]
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr90 = rotation(arr)
    arr180 = rotation(arr90)
    arr270 = rotation(arr180)
    print(f'#{tc}')
    for i in range(N):
        print(''.join(map(str, arr90[i])), ''.join(map(str, arr180[i])), ''.join(map(str, arr270[i])))
