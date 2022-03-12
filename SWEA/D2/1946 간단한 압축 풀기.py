import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    s = ''
    for i in range(N):
        alphabet, nums = input().split()
        s += alphabet * int(nums)
    print(f'#{tc}')
    while len(s) > 10:
        print(s[0:10])
        s = s[10:]
    print(s)
