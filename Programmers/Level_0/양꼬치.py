# https://school.programmers.co.kr/learn/courses/30/lessons/120830
def solution(n, k):
    j = n//10
    answer = n*12000 + (k-j)*2000 
    return answer