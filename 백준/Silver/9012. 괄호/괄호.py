from sys import stdin
input = stdin.readline


def check_right(parenthesis_list):
    stack = []
    for parenthesis in parenthesis_list:
        if parenthesis == "(":
            stack.append(parenthesis)
        else:   # parenthesis == ")"
            if stack:
                stack.pop()
            else:
                return 'NO'
    if stack:
        return 'NO'
    return 'YES'


T = int(input())    # 입력 데이터의 수

for tc in range(T):
    arr = list(input().rstrip())
    print(check_right(arr))