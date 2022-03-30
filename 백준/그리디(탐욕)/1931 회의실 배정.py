"""
11
1 4
3 5
1 2
5 7
3 8
5 9
6 10
8 12
8 11
2 13
12 14

"""
from sys import stdin

input = stdin.readline

N = int(input())  # N: 회의의 수
time = []
for i in range(N):
    a, b = map(int, input().split())
    time.append((a, b))

print(time)
time = sorted(time, key=lambda x: x[0])     # 시작시간 기준 오름차순 정렬
print(time)
time = sorted(time, key=lambda x: x[1])     # 종료시간 기준 오름차순 정렬
print(time)

end = cnt = 0
for i, j in time:   # i: 시작시간, j: 종료시간
    if i >= end:    # 지난 종료시간과 교차하지 않으면 회의 가능
        cnt += 1
        end = j
print(cnt)
