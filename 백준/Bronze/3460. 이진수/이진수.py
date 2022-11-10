import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    bits = []
    while N:
        bits.append(N % 2)
        # bits = str(N % 2) + bits
        N //= 2

    P = len(bits)
    for i in range(P):
        if bits[i]:
            print(i, end=' ')