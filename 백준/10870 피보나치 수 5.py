n = int(input())

memo = [0, 1]
for i in range(2, 21):
    memo.append(memo[i-2]+memo[i-1])
print(memo[n])