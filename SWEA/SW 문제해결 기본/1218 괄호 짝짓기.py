import sys
sys.stdin = open('input.txt')


def bracket(lst, n):
    item = {')': '(', '}': '{', ']': '[', '>': '<'}
    b = []
    for i in range(N):
        if lst[i] in item.values():
            b.append(lst[i])
        if lst[i] in item.keys():
            if b.pop() == item[lst[i]]:
                continue
            else:
                return 0
    return 1


for tc in range(1, 11):
    N = int(input())
    lst = list(input())
    print(f'#{tc} {bracket(lst, N)}')
