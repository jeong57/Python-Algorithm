def palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[-1-i]:
            return 0
        else:
            return 1

T = int(input())

for i in range(1, T+1):
    a = input()
    print(f'#{i} {palindrome(a)}')