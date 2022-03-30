"""
3 4
0000
0010
0000
1001
1011
1001

"""
"""
18 3
001
100
100
000
011
010
100
100
010
010
010
110
101
101
000
110
000
110
001
100
011
000
100
010
011
100
101
101
010
001
010
010
111
110
111
001

"""
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().rstrip())) for _ in range(N)]
B = [list(map(int, input().rstrip())) for _ in range(N)]

flag = 1
result = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:  # A, B가 하나라도 다르면 3x3 배열 단위로 바꾸기
            for k in range(i, i+3):
                for l in range(j, j+3):
                    A[k][l] = int(not A[k][l])  # 0 -> 1, 1 -> 0
            result += 1         # 바꾼 횟수 세기

# 배열을 다 돌았을 때도 A와 B가 같지 않다면 -1 출력
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            flag = 0
            break

print(result) if flag else print(-1)