T = int(input())
for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    min = (m1 + m2) % 60
    hour = (h1+h2)+(m1+m2)//60
    if hour % 12:
        hour = hour % 12
    else:
        hour = 12
    print(f'#{tc} {hour} {min}')