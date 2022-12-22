# https://school.programmers.co.kr/learn/courses/30/lessons/68644#
def solution(numbers):
    answer = []
    for idx, v1 in enumerate(numbers):
        for v2 in numbers[idx+1: ]:
            answer.append(v1+v2)
    return sorted(set(answer))


from itertools import combinations
def solution(numbers):
    answer = []
    combs = list(combinations(numbers, 2))
    for comb in combs:
        answer.append(sum(comb))
    
    answer = list(set(answer))
    answer.sort()

    return answer

