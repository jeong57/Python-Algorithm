"""
3
4
7
10

"""


from sys import stdin


n = int(input())
f = [0, 1, 2, 4]
for i in range(4, 12):
    f.append(sum(f[-3:]))
for _ in range(n):
    print(f[int(input())])

