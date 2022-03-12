# 방법 1
n = int(input())
f = [0, 1, 2]
for i in range(3, n+1):
    f.append(f[i-2]+f[i-1])
print(f[n] % 10007)

# 방법 2
n = int(input())
f = [0, 1, 2]
for i in range(3, 1001):
    f.append(f[i-2]+f[i-1])
print(f[n] % 10007)
