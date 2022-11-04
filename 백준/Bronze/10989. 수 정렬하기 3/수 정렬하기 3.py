import sys
input = sys.stdin.readline


N = int(input())
counts = [0] * 10001
arr = []

for i in range(N):
    counts[int(input())] += 1

for i in range(1, 10001):
    if counts[i]:
        for _ in range(counts[i]):
            print(i)