# 색종이 수
num = int(input())
# 도화지 면적
white = [[0]*101 for _ in range(101)]
for n in range(num):
    x, y = map(int, input().split())
    # 색종이 면적만큼 칠하기
    for i in range(x, x+10):
        for j in range(y, y+10):
            white[i][j] = 1
tot = 0
for i in range(101):
    for j in range(101):
        if white[i][j]:
            tot += 1
print(tot)