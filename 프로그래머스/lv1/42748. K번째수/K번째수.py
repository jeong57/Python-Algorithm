def solution(array, commands):
    answer = []
    for command in commands:
        start, end, temp = command
        lst = sorted(array[start-1 : end])
        answer.append(lst[temp-1])
    return answer