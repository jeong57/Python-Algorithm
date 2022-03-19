from sys import stdin
from collections import deque
input = stdin.readline


N = int(input())
Q = deque()
rear = front = -1
for i in range(N):
    cmd = list(input().rstrip().split())
    if cmd[0] == 'push':
        Q.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(Q.popleft()) if Q else print(-1)
    elif cmd[0] == 'size':
        print(len(Q))
    elif cmd[0] == 'empty':
        print(0) if Q else print(1)
    elif cmd[0] == 'front':
        print(Q[0]) if Q else print(-1)
    elif cmd[0] == 'back':
        print(Q[-1]) if Q else print(-1)


# N = int(input())
# Q = []
# rear = front = -1
# for i in range(N):
#     cmd = list(input().rstrip().split())
#     if cmd[0] == 'push':
#         Q.append(int(cmd[1]))
#     elif cmd[0] == 'pop':
#         print(Q.pop(0)) if Q else print(-1)
#     elif cmd[0] == 'size':
#         print(len(Q))
#     elif cmd[0] == 'empty':
#         print(0) if Q else print(1)
#     elif cmd[0] == 'front':
#         print(Q[0]) if Q else print(-1)
#     elif cmd[0] == 'back':
#         print(Q[-1]) if Q else print(-1)
