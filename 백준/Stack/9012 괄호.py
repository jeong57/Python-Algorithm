def bracket(lst):
    stack = []
    for i in lst:
        if i == '(':    # 여는 괄호이면 stack에 넣기
            stack.append(i)
        else:   # 닫는 괄호일 때
            if not stack:   # stack에서 뺄 게 없으면 no
                return 'NO'
            stack.pop() # 아니면 stack.pop()
    # for문 완료 후 stack이 비어있지 않으면
    if stack:
        return 'NO'
    # 비어있으면
    return 'YES'


N = int(input())
for _ in range(N):
    lst = list(input())
    print(bracket(lst))