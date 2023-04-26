# https://school.programmers.co.kr/learn/courses/30/lessons/12922
def solution(n):
    answer = []
    for i in range(n):
        if i%2 == 0:
            answer.append('수')
        else:
            answer.append('박')
    return ''.join(answer)

def solution(n):
    return ''.join('수박'[i%2] for i in range(n))