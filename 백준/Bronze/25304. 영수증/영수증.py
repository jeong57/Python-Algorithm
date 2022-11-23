import sys
input = sys.stdin.readline

X = int(input())    # 영수증에 적힌 총 금액
N = int(input())    # 영수증에 적힌 구매 물건 종류의 수
price = 0
for i in range(N):
    a, b = map(int, input().split())
    price += (a * b)

print('Yes') if X == price else print('No')