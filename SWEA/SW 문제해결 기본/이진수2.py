import sys
sys.stdin = open('이진수2_input.txt')

T = int(input())
for tc in range(1, T+1):
    n = float(input())
    result = ''
    flag = 0
    while n != 0:
        if len(result) >= 12:
            flag = 1
            break
        else:
            n = 2 * n
            result += str(int(n))
            n = n - int(n)
    if flag:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {result}')
    # print(f'#{tc} {n * 2 - int(n*2)}')
