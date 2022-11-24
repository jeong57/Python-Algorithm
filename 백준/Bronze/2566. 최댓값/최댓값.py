import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]   # 입력 행렬

fi, fj = 0, 0
max_result = -1
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_result:
            fi, fj = i+1, j+1
            max_result = arr[i][j]
print(max_result)
print(fi, fj)