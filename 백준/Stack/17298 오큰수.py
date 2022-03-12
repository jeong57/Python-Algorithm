"""
4
3 5 2 7

4
9 5 4 8

"""

N = int(input())
lst = list(map(int, input().split()))
stack = []
result = []
for i in range(N-1, -1, -1):    # 뒤에서부터 접근하기
    while stack and lst[i] >= stack[-1]:
        stack.pop()
    if not stack:
        result.append(-1)
        stack.append(lst[i])
    else:
        result.append(stack[-1])
        stack.append(lst[i])
print(*result[::-1])
