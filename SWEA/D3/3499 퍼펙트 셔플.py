"""
3
6
A B C D E F
4
JACK QUEEN KING ACE
5
ALAKIR ALEXSTRASZA DR-BOOM LORD-JARAXXUS AVIANA
"""
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cards = list(input().split())
#     result = []
#     for i in range((N+1)//2):
#         result.append(cards[i])
#         if (N + 1) // 2 + i < N:
#             result.append(cards[(N+1)//2+i])
#     print(f'#{tc}', *result)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(input().split())
    j = 1
    for i in range((N+1)//2, N):
        cards.insert(j, cards.pop(i))
        j += 2
    print(f'#{tc}', *cards)
