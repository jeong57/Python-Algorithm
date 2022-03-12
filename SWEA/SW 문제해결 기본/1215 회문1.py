import sys
sys.stdin = open('input.txt')


def palindrome(lst, n):
    for i in range(n//2):
        if lst[i] != lst[n-i-1]:
            return 0
    else:
        return 1


for test_case in range(1, 11):
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8-n+1):
            b = [arr[i][k] for k in range(j, j+n)]
            c = [arr[k][i] for k in range(j, j+n)]
            if palindrome(b, n):
                cnt += 1
            if palindrome(c, n):
                cnt += 1
    print(f'#{test_case} {cnt}')
