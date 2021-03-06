import sys
sys.stdin = open('subtree_input.txt')

# 전위 순회
def preorder(t):
    global cnt
    if t:
        cnt += 1
        preorder(arr[1][t])
        preorder(arr[2][t])


T = int(input())
for tc in range(1, T+1):
    # E: 간선 개수, N: 찾는 서브트리의 루트
    E, N = map(int, input().split())
    arr = [[i for i in range(E+2)], [0]*(E+2), [0]*(E+2)]
    # temp: 입력 노드 리스트
    temp = list(map(int, input().split()))
    for i in range(E):
        a, b = temp[2*i], temp[2*i+1]
        if arr[1][a] == 0:
            arr[1][a] = b
        else:
            arr[2][a] = b
    # cnt: 서브트리 노드 수
    cnt = 0
    preorder(N)
    print(f'#{tc} {cnt}')