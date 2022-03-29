import sys
sys.stdin = open('화물도크_input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # N: 신청서
    truck = [[] for _ in range(N)]  # (시작, 종료시간) 넣을 리스트
    time = []   # 각 화물차의 작업 시간 리스트
    visited = [0] * 25  # 작업 체크
    for i in range(N):
        s, e = map(int, input().split())
        truck[i] = (s, e)
        time.append(e-s)
    time.sort()     # 작업 시간 오름차순 정렬(작업 시간 작은 것부터 화물 운반)

    result = 0
    while time:
        dif = time.pop(0)   # dif: 각 화물차의 작업 시간(짧은 것부터)
        for i in range(len(truck)):
            if truck[i][1]-truck[i][0] == dif:
                s, e = truck.pop(i)
                if 1 not in visited[s:e]:
                    visited[s:e] = [1] * (e-s)
                    result += 1
                break
    print(f'#{tc} {result}')
