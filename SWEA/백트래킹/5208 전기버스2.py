import sys
sys.stdin = open('전기버스2_input.txt')


def bus(start, end, cnt):
    global min_value
    # 가지치기
    if cnt > min_value:
        return
    # 종료조건
    if end >= N-1:
        if cnt < min_value:
            min_value = cnt
        return
    else:
        for i in range(start+1, end+1):
            bus(i, i+arr[i], cnt+1)


T = int(input())
for tc in range(1, T+1):
    temp = list(map(int, input().split()))
    N = temp[0]
    arr = temp[1:]
    min_value = 987654321
    bus(0, arr[0], 0)    # 출발점, 종점, 개수
    print(f'#{tc} {min_value}')
