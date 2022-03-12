import sys
sys.stdin = open('input.txt')


for test_case in range(1, 11):
    dump = int(input())
    lst = list(map(int, input().split()))
    for i in range(dump):
        max_idx = min_idx = 0
        for j in range(100):
            if lst[j] > lst[max_idx]:
                max_idx = j
            elif lst[j] < lst[min_idx]:
                min_idx = j
        lst[max_idx] -= 1
        lst[min_idx] += 1

    max_value = min_value = lst[0]
    for i in range(100):
        if lst[i] > max_value:
            max_value = lst[i]
        elif lst[i] < min_value:
            min_value = lst[i]
    result = max_value - min_value
    print(f'#{test_case} {result}')
