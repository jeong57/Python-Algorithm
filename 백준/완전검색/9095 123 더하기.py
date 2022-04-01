"""
3
4
7
10

"""

import sys

memo = [0] * 11
memo[0:3] = [1, 1, 2]
for i in range(3, 11):
    memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

T = int(input())
for tc in range(1, T+1):
    N = int(sys.stdin.readline())
    print(memo[N])

