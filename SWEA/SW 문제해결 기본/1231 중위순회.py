import sys
sys.stdin = open("중위순회_input.txt")


def in_order(node):
    if node != 0:
        in_order(tree[node][2])
        print(tree[node][1], end='')
        in_order(tree[node][3])
    return


# 총 10개의 테스트케이스
for tc in range(1, 11):
    N = int(input())    # N: 노드의 수
    tree = [[0]*4 for _ in range(N+1)]
    arr = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        lst = list(input().split())
        arr[i] = lst + [0] * (4 - len(lst))
        arr[i][0] = int(arr[i][0])
        arr[i][2] = int(arr[i][2])
        arr[i][3] = int(arr[i][3])

    for i in range(1, N+1):
        num, value, c1, c2 = arr[i][:]
        tree[num][0:4] = [num, value, c1, c2]
    print(f'#{tc}', end=' ')
    in_order(1)
    print()
