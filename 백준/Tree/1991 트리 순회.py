"""
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

"""
# 완전이진트리가 아니기 때문에 2차 배열 사용해야 함.
# 아스키코드: A=65 ~ Z=90
# ord('A')=65

from sys import stdin
input = stdin.readline


def preorder(n):
    if n:
        print(chr(n+64), end='')
        preorder(c1[n])
        preorder(c2[n])


def inorder(n):
    if n:
        inorder(c1[n])
        print(chr(n + 64), end='')
        inorder(c2[n])


def postorder(n):
    if n:
        postorder(c1[n])
        postorder(c2[n])
        print(chr(n + 64), end='')


N = int(input())
p = [''] * (N+1)    # 부모노드
c1 = [0] * (N+1)   # 왼쪽 자식노드
c2 = [0] * (N+1)   # 오른쪽 자식노드
for i in range(1, N+1):
    a, b, c = input().rstrip().split()
    node = ord(a)-64
    if b != '.':
        c1[node] = ord(b) - 64
    if c != '.':
        c2[node] = ord(c) - 64
preorder(1)
print()
inorder(1)
print()
postorder(1)
