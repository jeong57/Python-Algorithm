import sys
sys.stdin = open('input.txt')


for test_case in range(1, 11):
    # n: 가로 길이 (빌딩의 최대 높이는 255)
    n = int(input())
    arr = list(map(int, input().split()))
    side = [-2, -1, 1, 2]
    tot = 0
    for i in range(2, n-2):
        min_value = 255
        for k in range(4):
            if arr[i]-arr[i+side[k]] <= 0:
                flag = 0
                break
            else:
                if arr[i]-arr[i+side[k]] < min_value:
                    flag = 1
                    min_value = arr[i]-arr[i+side[k]]
        if flag:
            tot += min_value
    print(f'#{test_case} {tot}')
