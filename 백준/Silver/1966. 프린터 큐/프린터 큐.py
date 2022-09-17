from sys import stdin
from collections import deque
input = stdin.readline

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    q = deque()     # 중요도 담을 큐
    idx = deque()   # 인덱스 담을 큐
    result = []
    sp = list(map(int, input().split()))
    for i in range(N):
        q.append(sp[i])
        idx.append(i)

    while q:
        # 중요도가 max가 아니면 뒤에 붙이기
        if q[0] != max(q):
            q.append(q.popleft())
            idx.append(idx.popleft())
        # 중요도가 max이면 result에 index 넣기
        else:
            q.popleft()
            result.append(idx.popleft())
    # index는 0부터 시작하므로 결괏값은 1 더해주기
    print(result.index(M)+1)