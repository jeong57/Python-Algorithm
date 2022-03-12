import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    s = list(input())
    for i in range(10):
        if s[0: i+1] == s[i+1:2*i+2]:
            madi = i+1
            break
    print(f'#{tc} {madi}')

# arr = ['k','o','r','e','a','k','o','r','e','a']
# print(arr[0:5] == arr[5:10])
