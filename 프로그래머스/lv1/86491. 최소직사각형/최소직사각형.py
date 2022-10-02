def solution(sizes):
    width_list = []
    height_list = []
    for size in sizes:
        width_list.append(max(size))
        height_list.append(min(size))

    answer = max(width_list) * max(height_list)
    return answer