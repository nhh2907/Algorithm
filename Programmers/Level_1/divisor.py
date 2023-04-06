# https://school.programmers.co.kr/learn/courses/30/lessons/12910
def solution(arr, divisor):
    answer = []
    for num in arr:
        if num%divisor==0:
            answer.append(num)
    if not len(answer):
        return [-1]
    return sorted(answer)

# best
def solution(arr, divisor):
    return sorted([num for num in arr if num%divisor == 0]) or [-1]