import sys
sys.stdin = open('컨테이너 운반_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 컨테이너 수, M: 트럭 수
    wi = list(map(int, input().split()))    # wi: 화물의 무게
    ti = list(map(int, input().split()))    # ti: 트럭의 적재용량
    visited = [0] * N   # 컨테이너를 운반했는지 여부 체크

    load = 0
    for i in range(M):
        std = ti[i]
        flag = 0
        idx = value = 0
        for j in range(N):
            if std >= wi[j] > value and not visited[j]:
                idx = j
                value = wi[j]
                flag = 1
        if flag:
            visited[idx] = 1
            load += value

    print(f'#{tc} {load}')
