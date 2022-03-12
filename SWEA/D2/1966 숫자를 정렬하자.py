def selection_sort(a, n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    selection_sort(arr, N)
    print(f'#{tc}', end=' ')
    for i in arr:
        print(i, end=' ')
    print()