"""
8
4
3
6
8
7
5
2
1

"""

from sys import stdin
input = stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]

stack = []
result = []
flag = 0
start = 1
for num in lst:
    # stack에 list 값 이하인 숫자 넣기
    for i in range(start, num+1):
        stack.append(i)
        result.append('+')
    # start 숫자 바꾸기(최대값으로 갱신)
    s = num + 1
    if s > start:
        start = s
    # stack의 마지막 값이 list의 값과 같을 때
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    # 같지 않다면 no
    else:
        flag = 1
        break
if flag:
    print('NO')
else:
    for i in result:
        print(i)
