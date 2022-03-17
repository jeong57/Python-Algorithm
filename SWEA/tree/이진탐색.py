import sys
sys.stdin = open('이진탐색_input.txt')


def inorder(i):    # i: node 번호
    global value
    if i <= N:
        inorder(i*2)        # 왼쪽 자식노드
        tree[i] = value
        value += 1
        inorder(i*2 + 1)    # 오른쪽 자식노드


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    value = 1   # 1~N 값 넣을 예정
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
