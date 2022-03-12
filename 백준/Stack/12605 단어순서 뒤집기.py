"""
3
this is a test
foobar
all your base
"""

from sys import stdin
input = stdin.readline

N = int(input())    # N: 전체 케이스 개수
for case in range(1, N+1):
    lst = list(input().split())
    result = lst[-1::-1]
    print(f'Case #{case}: ', end='')
    print(' '.join(result))