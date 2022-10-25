N = int(input())    # N: 정수 배열의 길이
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()
result = 0
for i in range(N):
    result += (A[i] * B[i])
print(result)