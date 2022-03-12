switch = int(input())
lst = list(map(int, input().split()))
student = int(input())
for i in range(student):
    # gender: 학생의 성별, n: 학생이 받은 수
    gender, n = map(int, input().split())
    if gender == 1:
        for j in range(n-1, switch, n):
            lst[j] = int(not(lst[j]))
    else:
        # 양옆으로 동일한 범위 구하기
        rng = 0
        for j in range(n):
            if (n-1+j) < switch and lst[n-1-j] == lst[n-1+j]:
                rng += 1
            else:
                break
        for j in range(n-rng, n+rng-1):
            lst[j] = int(not(lst[j]))

while len(lst) > 20:
    for i in range(20):
        print(lst[i], end=' ')
    lst = lst[20:]
    print()
print(*lst)