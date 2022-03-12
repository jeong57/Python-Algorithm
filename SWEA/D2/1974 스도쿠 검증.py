import sys
sys.stdin = open('input.txt')


def sudoku(arr):
    for i in range(9):
        b = [arr[i][j] for j in range(9)]
        c = [arr[j][i] for j in range(9)]
        for k in range(1, 10):
            if k not in b or k not in c:
                return 0
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            d = [arr[i+k][j+l] for k in range(3) for l in range(3)]
            for m in range(1, 10):
                if m not in d:
                    return 0
    return 1


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{tc} {sudoku(arr)}')
