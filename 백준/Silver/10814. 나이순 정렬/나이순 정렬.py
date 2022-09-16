from sys import stdin
input = stdin.readline

N = int(input())
arr = []
for i in range(N):
    age, name = input().rstrip().split()
    age = int(age)
    arr.append([age, name])

arr.sort(key=lambda x: x[0])
for i in range(N):
    print(*arr[i])