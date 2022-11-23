N = int(input())    # 정수의 개수
arr = list(map(int, input().split()))
nums = [0] * 201    # -100~100까지 배열 만들어주기(0 포함)
for i in range(N):
    nums[arr[i]+100] += 1
print(nums[int(input())+100])
