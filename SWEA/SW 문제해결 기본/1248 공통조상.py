import sys
sys.stdin = open("공통조상_input.txt")


def find_root(node):
    roots = []
    while tree[node][2] > 0:
        roots.append(tree[node][2])
        node = tree[node][2]
    return roots


def pre_order(node):
    global cnt
    if node != 0:
        cnt += 1
        pre_order(tree[node][0])
        pre_order(tree[node][1])
    return cnt


T = int(input())
for tc in range(1, T+1):
    # V: 노드 수, E: 간선 수/ a, b: 공통조상을 찾는 노드 번호
    V, E, a, b = map(int, input().split())
    tree = [[0]*3 for _ in range(V+1)]
    temp = list(map(int, input().split()))
    for i in range(E):
        p, c = temp[i*2], temp[i*2+1]
        if not tree[p][0]:  # 첫 번째 자식이 없으면
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p

    # 공통조상 구하기
    a_roots = find_root(a)
    b_roots = find_root(b)
    for i in a_roots:
        if i in b_roots:
            same_root = i
            break
    # 공통조상을 루트로 하는 서브트리 개수
    cnt = 0
    nodes = pre_order(same_root)
    print(f'#{tc} {same_root} {nodes}')
