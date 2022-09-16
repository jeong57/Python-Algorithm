import sys
input = sys.stdin.readline


N = int(input())
lst = list(input().rstrip() for _ in range(N))
lst = list(set(lst))    # 중복 제거

lst.sort()
lst.sort(key=lambda x: len(x))
for word in lst:
    print(word)
