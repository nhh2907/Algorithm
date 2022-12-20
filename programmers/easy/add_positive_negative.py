# https://school.programmers.co.kr/learn/courses/30/lessons/76501?language=python3
def solution(absolutes, signs):
    answer = 0
    for num in zip(absolutes, signs):
        if num[1] == True:
            answer += num[0]
        else:
            answer -= num[0]
    return answer

# Short coding
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
    
