import sys
input = sys.stdin.readline

arr = [0] * 30
for i in range(28):
    arr[int(input())-1] = 1

for i in range(30):
    if not arr[i]:
        print(i+1)