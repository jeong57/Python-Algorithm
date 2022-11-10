# A: 수, B: 약수 순서
A, B = map(int, input().split())

cnt = 0
for i in range(1, A+1):
    if A % i == 0:
        cnt += 1
        if cnt == B:
            print(i)
if cnt < B:
    print(0)