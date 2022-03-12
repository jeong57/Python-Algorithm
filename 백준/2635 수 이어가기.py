n = int(input())
max_value = 0
result = []
for i in range(1, n+1):
    lst = [n, i]
    j = 2
    while (lst[j-2]-lst[j-1]) >= 0:
        lst.append(lst[j-2] - lst[j-1])
        j += 1
    if len(lst) > max_value:
        result = lst
        max_value = len(lst)

print(max_value)
print(*result)
