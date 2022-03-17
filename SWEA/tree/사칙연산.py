import sys
sys.stdin = open("사칙연산_input.txt")


def postorder(n):   # n: 노드번호
    # 노드번호가 N 이하이고 자식 노드가 있으면
    if n <= N and c1[n] and c2[n]:
        postorder(c1[n])
        postorder(c2[n])
        # 실수로 계산하고 마지막에 정수로 출력
        if operator[n] == '+':
            operand[n] = operand[c1[n]] + operand[c2[n]]
        elif operator[n] == '-':
            operand[n] = operand[c1[n]] - operand[c2[n]]
        elif operator[n] == '*':
            operand[n] = operand[c1[n]] * operand[c2[n]]
        elif operator[n] == '/':
            operand[n] = operand[c1[n]] / operand[c2[n]]
    return


T = 10
for tc in range(1, T+1):
    N = int(input())
    operator = ['']*(N+1)   # 연산자
    c1 = [0] * (N+1)        # 왼쪽 자식노드
    c2 = [0] * (N+1)        # 오른쪽 자식노드
    operand = [0] * (N+1)   # 피연산자
    for i in range(N):
        lst = list(input().split())
        num = int(lst[0])
        if len(lst) == 4:
            operator[num] = lst[1]
            c1[num] = int(lst[2])
            c2[num] = int(lst[3])
        elif len(lst) == 2:
            operand[num] = int(lst[1])
    postorder(1)
    print(f'#{tc} {int(operand[1])}')
