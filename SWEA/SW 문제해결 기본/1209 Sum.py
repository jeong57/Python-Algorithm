import sys
sys.stdin = open('input.txt')

for _ in range(10):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_value = 0
    for i in range(100):
        cnt_r = cnt_c = 0
        for j in range(100):
            cnt_r += arr[i][j]
            cnt_c += arr[j][i]
        cnt_x = cnt_y = 0
        cnt_x += arr[i][i]
        cnt_y += arr[i][99-i]
        if cnt_r > max_value:
            max_value = cnt_r
        if cnt_c > max_value:
            max_value = cnt_c
        if cnt_x > max_value:
            max_value = cnt_x
        if cnt_y > max_value:
            max_value = cnt_y
    print(f'#{test_case} {max_value}')
