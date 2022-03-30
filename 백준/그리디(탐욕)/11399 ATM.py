"""
5
3 1 4 3 2

"""
# 1 <= N <= 1,000 이니까 재귀 쓰지 말자.

N = int(input())    # N: 사람의 수
lst = list(map(int, input().split()))
lst.sort()  # 오름차순 정렬하기

result = 0
for i in range(N, 0, -1):
    result += lst[N-i] * i
print(result)
