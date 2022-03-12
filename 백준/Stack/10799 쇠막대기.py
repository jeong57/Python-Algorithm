"""
()(((()())(())()))(())
(((()(()()))(())()))(()())
"""

lst = list(input())
# cnt: 현재 잘린 막대 수, tot: 총 잘린 막대 수
cnt = tot = 0
for i in range(len(lst)):
    # 쇠막대기 시작이면 cnt += 1
    if lst[i] == '(':
        cnt += 1
    # ")"이면 레이저인지 막대 끝인지 구분
    else:
        cnt -= 1
        # 막대 끝이면 tot += 1
        if lst[i-1] == ')':
            tot += 1
        # 레이저면 tot += 현재 막대 수
        else:
            tot += cnt
print(tot)
