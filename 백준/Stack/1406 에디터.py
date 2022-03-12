from sys import stdin

lst = list(stdin.readline().rstrip())
N = int(stdin.readline())
# 빈 스택 만들기
stack = []
for _ in range(N):
    cmd = list(stdin.readline().rstrip().split())
    # L : 커서를 왼쪽으로 한 칸 이동 = stack.append
    if cmd[0] == 'L':
        if lst:
            stack.append(lst.pop())
    # D : 커서를 오른쪽으로 한 칸 이동 = lst.append
    elif cmd[0] == 'D':
        if stack:
            lst.append(stack.pop())
    # B : 커서 왼쪽 문자 삭제
    elif cmd[0] == 'B':
        if lst:
            lst.pop()
    # P : 커서 왼쪽에 문자 추가 = lst.append
    elif cmd[0] == 'P':
        lst.append(cmd[1])

print(''.join(lst+stack[::-1])) # stack은 순서가 거꾸로 돼 있음.
