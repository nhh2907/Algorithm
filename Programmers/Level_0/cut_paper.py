# https://school.programmers.co.kr/learn/courses/30/lessons/120922?language=python3
def solution(M, N):
    a = M-1
    b = M*(N-1)
    return a+b

# best
def solution(M, N):
    return (M*N)-1  # M*(N-1) + M-1를 전개