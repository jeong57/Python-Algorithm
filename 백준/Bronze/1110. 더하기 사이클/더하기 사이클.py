num = int(input())

digit_tot = 0
first_num = num
result = 10 * (num % 10)
if num < 10:
    digit_tot = num
else:
    while num:
        digit_tot += num % 10
        num //= 10

result += (digit_tot % 10)
cycle = 1

while result != first_num:
    spare = result
    digit_tot = 0
    while spare:
        digit_tot += spare % 10
        spare //= 10
    result = (result % 10) * 10 + digit_tot % 10
    cycle += 1
print(cycle)