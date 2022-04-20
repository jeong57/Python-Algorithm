"""
121
1231
12421
0

"""


def palindrome(n):
    global flag
    for i in range(len(n)//2):
        if n[i] != n[-1-i]:
            flag = 0
            return flag
    return flag


while True:
    num = input()
    if num == '0':
        break
    else:
        flag = 1
        num = list(map(int, num))
        palindrome(num)
        print('yes') if flag else print('no')
