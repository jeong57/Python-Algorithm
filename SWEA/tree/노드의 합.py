import sys
sys.stdin = open("노드의 합_input.txt")


def postorder(n):   # 후위순회
    if n <= N:
        postorder(n*2)      # 왼쪽 자식노드
        postorder(n*2+1)    # 오른쪽 자식노드
        if n*2+1 <= N:      # 자식노드가 2개인 경우
            tree[n] = tree[n*2] + tree[n*2+1]
        elif n*2 <= N:      # 자식노드가 1개인 경우(완전이진트리니까 왼쪽부터 채워짐)
            tree[n] = tree[n*2]


T = int(input())
for tc in range(1, T+1):
    # N: 노드 개수, M: 리프노드 개수, L: 값 출력할 노드
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)  # 완전 이진트리 => 1차원 리스트
    for i in range(M):
        a, b = map(int, input().split())
        tree[a] = b
    postorder(1)
    print(f'#{tc} {tree[L]}')
