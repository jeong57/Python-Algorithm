def IsPalindrome(s):
    return recursion(s, 0, len(s)-1)


def recursion(s, l, r):     # s: 문자열, l: 시작, r: 끝
    global count
    count += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)


T = int(input())    # 테스트케이스의 수
for _ in range(T):
    count = 0       # recursion 함수의 호출 횟수
    print(IsPalindrome(input()), end=' ')
    print(count)