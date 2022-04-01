"""
3
1 2 3

"""

N = int(input())
lst = map(int, input().split())
visited = [0] * 101
result = 0
for i in lst:
    if visited[i]:
        result += 1
    else:
        visited[i] = 1
print(result)
