"""
24 18

"""


# 최소공배수, n1 > n2
def find_min(n1, n2):
    num = n1
    while True:
        if num % n2 == 0:
            return num
        num += n1


# 최대공약수, n1 > n2
def find_max(n1, n2):
    i = n2
    while True:
        if n1 % i == 0 and n2 % i == 0:
            return i
        i -= 1


a, b = map(int, input().split())

if a > b:
    result1 = find_max(a, b)
    result2 = find_min(a, b)
else:
    result1 = find_max(b, a)
    result2 = find_min(b, a)
print(result1)
print(result2)
