import sys

arr = []
N = int(sys.stdin.readline())
for n in range(N):
    arr.append(int(sys.stdin.readline()))
# 맨 오른쪽에서 보는 막대의 높이
first = arr.pop()
# 보이는 막대 수(맨 오른쪽도 포함)
cnt = 1

# 막대기를 다 확인할 때까지 반복
while arr:
    # 뒤에 막대가 앞 막대보다 작거나 같으면 제거
    if arr[-1] <= first:
        arr.pop()
    # 뒤에 막대가 앞 막대보다 크면 cnt += 1
    # 이제 뒤에 있던 막대가 기준 막대가 됨
    else:
        first = arr.pop()
        cnt += 1
print(cnt)