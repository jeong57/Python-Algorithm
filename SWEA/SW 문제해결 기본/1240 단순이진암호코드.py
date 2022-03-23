import sys
sys.stdin = open("단순이진암호코드_input.txt")


table = [
    [0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 1]]


def find_end(N, M, arr):
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j]:
                ei, ej = i, j
                return ei, ej


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    ei, ej = find_end(N, M, arr)    # 암호코드 끝자리 인덱스 찾기
    cnt = 1     # 코드 자리 번호
    check = 0   # 검증 코드
    result = 0  # 암호 코드 숫자의 합
    for i in range(ej-55, ej+1, 7):
        temp = arr[ei][i:i+7]
        num = table.index(temp)
        result += num
        check += num*3 if cnt % 2 else num
        cnt += 1
    if check % 10:  # 검증과정
        result = 0
    print(f'#{tc} {result}')
