import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    ai = P * W
    if W <= R:
        bi = Q
    else:
        bi = Q + (W-R)*S
    if ai > bi:
        print(f'#{tc} {bi}')
    else:
        print(f'#{tc} {ai}')
