# https://school.programmers.co.kr/learn/courses/30/lessons/120924
def solution(common):
    diff_1 = common[1] - common[0]
    diff_2 = common[2] - common[1]
    
    if diff_1 - diff_2 == 0:
        answer = common[-1] + diff_1
    else: 
        answer = (common[1] // common[0]) * common[-1]
    return answer
