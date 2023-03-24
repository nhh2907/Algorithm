# https://school.programmers.co.kr/learn/courses/30/lessons/68644#
def solution(numbers):
    answer = []
    for idx, v1 in enumerate(numbers):
        for v2 in numbers[idx+1: ]:
            answer.append(v1+v2)
    return sorted(set(answer))


# 조합 만들기 방법 1
def solution(numbers):
	idx = [(i,j) for i in range(len(numbers)) for j in range(len(numbers)) if i<j]
	answer = set([numbers[i]+numbers[j] for i,j in idxs])
	return = answer


# 조합 만들기 방법 2
from itertools import combinations
def solution(numbers):
    answer = []
    combs = list(combinations(numbers, 2))
    for comb in combs:
        answer.append(sum(comb))
    
    answer = list(set(answer))
    answer.sort()

    return answer

