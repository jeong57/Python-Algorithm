from sys import stdin
input = stdin.readline


K = int(input())
stack = []
for i in range(K):
    num = int(input())
    stack.append(num) if num else stack.pop()

print(sum(stack))