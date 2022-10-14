import sys
input = sys.stdin.readline

N = int(input())    # N: 숫자 카드의 개수
cards = list(map(int, input().split()))     # 숫자 카드에 적혀있는 정수
M = int(input())    # M: 가지고 있는지 판단할 숫자 카드 수
wants = list(map(int, input().split()))     # 가지고 있는지 판단할 숫자

arr = [0] * 20000001
for i in range(N):
    arr[cards[i]+10000000] = 1

for i in range(M):
    if arr[wants[i]+10000000]:
        print(1, end=' ')
    else:
        print(0, end=' ')