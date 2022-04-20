"""
5 2

"""

N, K = map(int, input().split())
result1 = 1
result2 = 1
for i in range(N, N-K, -1):
    result1 *= i
    result2 *= (N-i+1)
print(result1//result2)