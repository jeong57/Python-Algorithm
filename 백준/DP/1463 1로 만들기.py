"""
2

10

"""

n = int(input())
f = [0, 0, 1, 1]
if n >= 4:
    for i in range(4, n+1):
        if not i % 2 and i % 3: # 2로 나누어떨어지고 3으로는 x
            f.append(min(f[i//2], f[i-1])+1)
        elif not i % 3 and i % 2:   # 3으로 나누어떨어지고 2로는 x
            f.append(min(f[i//3], f[i-1])+1)
        elif not i % 3 and not i % 2:   # 6의 배수
            f.append(min(f[i//3], f[i//2])+1)
        else:   # 2, 3 모두 나누어떨어지지 않음
            f.append(min(f[i-1]+1, f[i-2]+2))
print(f[n])