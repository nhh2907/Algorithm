# https://school.programmers.co.kr/learn/courses/30/lessons/147355?language=python3
def solution(t, p):
    answer = 0
    for i in range(0, len(t)-len(p)+1):
        cp = t[i:len(p)+i]
        if int(cp) <= int(p):
            answer += 1
    return answer