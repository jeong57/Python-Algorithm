"""
4
1 3 5 7

"""


# 어떠한 자연수의 배수들을 모두 배열에서 체크하기
# 체크된 수는 무조건 1과 자기 자신이 아닌 약수가 존재
# 즉 소수가 아님
def not_prime(n):
    value = n
    while value+n <= 1000:
        value += n
        dp[value] = 1


# 수는 1000 이하의 자연수
dp = [0] * 1001
for i in range(2, 10001):
    not_prime(i)

N = int(input())
arr = list(map(int, input().split()))
cnt = 0
# 소수는 1이 아닌 자연수 중 약수가 1과 자기 자신인 것
for i in range(N):
    if arr[i] != 1 and not dp[arr[i]]:
        cnt += 1
print(cnt)
