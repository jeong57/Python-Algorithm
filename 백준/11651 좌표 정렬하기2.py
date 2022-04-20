"""
5
0 4
1 2
1 -1
2 2
3 3

"""


from sys import stdin
input = stdin.readline


N = int(input())
lst = []
for _ in range(N):
    a, b = map(int, input().split())
    lst.append([a, b])

lst.sort(key=lambda x: (x[1], x[0]))
for i in range(N):
    print(*lst[i])
