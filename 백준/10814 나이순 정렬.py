"""
3
21 Junkyu
21 Dohyun
20 Sunyoung

"""
from sys import stdin
input = stdin.readline

N = int(input())
arr = []
for i in range(N):
    age, name = input().rstrip().split()
    arr.append([i, int(age), name])

arr.sort(key=lambda x: (x[1], x[0]))
for i in range(N):
    print(arr[i][1], arr[i][2])
