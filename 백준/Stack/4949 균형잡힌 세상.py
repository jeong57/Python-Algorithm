"""
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.

"""
from sys import stdin
input = stdin.readline


while True:
    s = input().rstrip()
    # 점 하나가 들어오면 입력의 종료조건
    if s == '.':
        break
    stack = []
    bracket = {')': '(', ']': '['}
    flag = 'yes'
    for chr in s:
        # (, [ 이면 스택에 넣기
        if chr in bracket.values():
            stack.append(chr)
        # ), [ 일 때
        elif chr in bracket.keys():
            # 스택이 비어있지 않고 마지막 원소가 value 값이라면 pop
            if stack and stack[-1] == bracket[chr]:
                stack.pop()
            # 스택이 비어있거나 마지막 원소가 value 값이 아니면 no
            else:
                flag = 'no'
                break
    if stack:
        flag = 'no'
    print(flag)
