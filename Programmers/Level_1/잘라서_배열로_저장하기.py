# https://school.programmers.co.kr/learn/courses/30/lessons/120913
def solution(my_str, n):
    answer = [my_str[n*i:(n+i*n)] for i in range(len(my_str)//n)]
    if len(my_str)%n:
        answer.append(my_str[len(''.join(answer)):])
    return answer

def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]