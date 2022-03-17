import sys
sys.stdin = open("이진 힙_input.txt")


def enq(item):
    global last
    last += 1
    tree[last] = item
    c = last        # 자식노드 번호
    p = last // 2   # 부모노드 번호
    while p > 0 and tree[p] > tree[c]:  # 최소힙
        tree[p], tree[c] = tree[c], tree[p]
        c = p       # 위로 올라가기
        p = c // 2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    temp = list(map(int, input().split()))  # 입력 리스트
    tree = [0] * (N+1)
    last = 0    # 힙의 원소의 개수(= 노드번호)
    # 최소 heap 만들기
    for i in temp:
        enq(i)
    # 조상노드 합 구하기
    i = N // 2
    result = 0
    while i >= 1:
        result += tree[i]
        i //= 2
    print(f'#{tc} {result}')