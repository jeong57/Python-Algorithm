"""
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

"""
N = int(input())
cur_cards = list(map(int, input().split()))
M = int(input())
find_cards = list(map(int, input().split()))

cards = [0] * (10000000*2+1)

for i in range(N):
    cards[cur_cards[i]-10000001] += 1

for j in range(M):
    print(cards[find_cards[j]-10000001], end=' ')
