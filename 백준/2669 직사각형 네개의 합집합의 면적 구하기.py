"""
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6
"""

arr = [[0]*101 for _ in range(101)]
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            arr[j][k] = 1
tot = 0
for i in range(101):
    for j in range(101):
        if arr[i][j]:
            tot += 1
print(tot)