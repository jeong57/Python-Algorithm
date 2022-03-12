T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    numbers.remove(max(numbers))
    numbers.remove(min(numbers))
    avg = sum(numbers) / len(numbers)

    print(f'#{i} {round(avg)}')