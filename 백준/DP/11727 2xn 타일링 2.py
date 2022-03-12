n = int(input())
f = [0, 1, 3]
for i in range(3, n+1):
    f.append(2*f[i-2]+f[i-1])
print(f[n] % 10007)
