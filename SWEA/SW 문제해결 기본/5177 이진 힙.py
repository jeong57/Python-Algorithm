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


def deq():
    global last
    tmp = tree[1]
    tree[1] = tree[last]
    last -= 1   # pop 하지 않고 그냥 마지막 노드 번호를 쓰지 않는다.
    p = 1   # 부모는 항상 루트노드(1)
    c = p * 2   # 왼쪽 자식
    while c <= last:
        # 오른쪽 자식이 있으면 왼쪽, 오른쪽 비교해서 대표 자식노드 선정
        if c+1 <= last and tree[c] > tree[c+1]:
            c = c+1
        if tree[p] > tree[c]:   # 부모와 자식 비교(최소힙)
            tree[p], tree[c] = tree[c], tree[p]
            p = c       # 밑으로 내려가기
            c = p * 2
        else:
            break
    return tmp
    
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    temp = list(map(int, input().split()))  # 입력 리스트
    tree = [0] * (N+1)
    last = 0    # 힙의 원소의 개수(= 노드번호)
    # 최소 heap 만들기
    for i in temp:
        enq(i)
    # print(tree)
    # deq()
    # print(tree)
    # 조상노드 합 구하기
    i = N // 2
    result = 0
    while i >= 1:
        result += tree[i]
        i //= 2
    print(f'#{tc} {result}')
