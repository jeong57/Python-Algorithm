import sys
sys.stdin = open("이진수1_input.txt")

# A: 65 ~ F: 70
# print(ord('F'))

table = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

T = int(input())
for tc in range(1, T+1):
    N, code = input().split()
    N = int(N)
    result = 0
    print(f'#{tc}', end=' ')
    for c in code:
        if 'A' <= c <= 'F':
            print(table[ord(c)-55], end='')
        else:
            print(table[int(c)], end='')
    print()
