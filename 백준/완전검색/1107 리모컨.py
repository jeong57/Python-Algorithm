"""
5457
3
6 7 8

"""
"""
500000
8
0 2 3 4 6 7 8 9

"""
N = int(input())    # N: 이동하려고 하는 채널
M = int(input())    # M: 고장난 버튼 개수
lst1 = list(range(10))

# 고장나지 않은 리모콘 번호 정리하기
if M:
    lst = list(map(int, input().split()))
    remote = list(set(lst1) - set(lst))
else:
    remote = list(range(10))

result = abs(100-N)     # 결과의 최댓값(모두 +, 또는 모두 -)
for i in range(1000001):    # +, - 50만개씩
    num = str(i)
    for j in range(len(num)):
        # 숫자의 각 자리 번호가 리모컨에서 고장났는지 체크
        # 고장났으면 그 숫자는 리모컨으로 만들지 못한다.
        if int(num[j]) not in remote:
            break
        # 숫자의 끝까지 다 입력할 수 있으면
        # 리모컨으로 누른 횟수 + (+ 또는 -로 나머지 번호를 채운 횟수)와 기존 결과값을 비교
        elif j == len(num)-1:
            result = min(result, len(num)+abs(int(num)-N))
print(result)
