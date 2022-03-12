"""
5
6 9 5 7 4

"""

N = int(input())
# 입력 리스트에 인덱스 추가(1부터 시작)
lst = [(idx, j) for idx, j in enumerate(list(map(int, input().split())), start=1)]
# 수신탑 높이를 담을 곳
stack = []
# 결과 인덱스를 담을 곳
result = []
for top in lst:
    if not stack:
        stack.append(top)
        result.append(0)
    else:
        while stack:
            # stack에 있는 탑의 높이가 list 값 이상이면
            if stack[-1][1] >= top[1]:
                result.append(stack[-1][0])
                break
            # stack에 있는 탑의 높이가 list 값보다 작으면
            else:
                stack.pop()
        # stack이 비어있으면 결과에 0 추가
        if not stack:
            result.append(0)
        # 탑 높이를 stack에 추가
        stack.append(top)

print(*result)
