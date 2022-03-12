from sys import stdin
input = stdin.readline

K = int(input())
# 빈 스택 만들기
stack = []
for _ in range(K):
    # 입력이 0이 아니면 stack.append
    n = int(input())
    if n:
        stack.append(n)
    # 입력이 0일 때
    else:
        # stack이 비어있지 않으면 stack.pop()
        if stack:
            stack.pop()

tot = 0
for i in range(len(stack)):
    tot += stack[i]
print(tot)
