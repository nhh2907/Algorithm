def solution(array, n):
    box = {}
    for num in array:
        box[num] = abs(n - num)
    box = sorted(box.items(), key = lambda x : (x[1], x[0]))

    return box[0][0]
