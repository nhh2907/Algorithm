# https://school.programmers.co.kr/learn/courses/30/lessons/12918
def solution(s):
    if len(s)==4 or len(s)==6:
        return s.isdigit() 
    else:
        return False

# best   
def solution(s):
    return s.isdigit() and len(s) in (4, 6)