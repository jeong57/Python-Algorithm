"""
3
ABAB
AABB
ABBA

"""

from sys import stdin


def good(words):
    stack = []
    for word in words:
        # 스택이 비어있으면 넣기
        if not stack:
            stack.append(word)
        else:
            if word == stack[-1]:
                stack.pop()
            else:
                stack.append(word)
    # stack이 남아있으면 0, 비어있으면 1(good) 반환
    return 0 if stack else 1


N = int(input())
lst = [stdin.readline().rstrip() for _ in range(N)]
cnt = 0
for i in lst:
    cnt += good(i)
print(cnt)
