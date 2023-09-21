def solution(sizes):
    width = 0
    height = 0
    for size in sizes:
        if max(size) > width:
            width = max(size)
        else:
            pass
        if min(size) > height:
            height = min(size)

    return width * height