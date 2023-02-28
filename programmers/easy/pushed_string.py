# https://school.programmers.co.kr/learn/courses/30/lessons/120921?language=python3#
def solution(A, B):
    check = A
    for num in range(len(A)):
        if A == B: break
        A = A[-1]+A[:-1]
    
    if num == 0:
        answer = 0
    elif check == A:
        answer = -1
    else:
        answer = num
    return answer

# best 1
def solution(A, B):
    check = A
    answer = 0
    while A != B:
        A = A[-1]+A[:-1]
        answer += 1
        if check == A:
            return -1
        else:
            continue
    return answer

# best 2
solution = lambda A, B: (B*2).find(A)