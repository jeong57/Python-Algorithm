import sys
sys.stdin = open('베이비진 게임_input.txt')


def perm(n, k, arr):
    if n == k:
        global flag
        if (p[0] == p[1] and p[1] == p[2]) or (p[0] + 1 == p[1] and p[1] + 1 == p[2]):
            flag = 1
            return
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = arr[i]
                perm(n, k+1, arr)
                visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []
    flag = 0
    for i in range(6):
        player1.append(cards[i*2])
        if len(player1) >= 3:
            N = len(player1)
            p = [0] * N
            visited = [0] * N
            perm(N, 0, player1)
            if flag:
                print(f'#{tc} 1')
                break
        player2.append(cards[i*2+1])
        if len(player2) >= 3:
            N = len(player2)
            p = [0] * N
            visited = [0] * N
            perm(N, 0, player2)
            if flag:
                print(f'#{tc} 2')
                break
    if not flag:
        print(f'#{tc} 0')
