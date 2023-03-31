# https://school.programmers.co.kr/learn/courses/30/lessons/12919
def solution(seoul):
    for i, element in enumerate(seoul):
        if element == 'Kim':
            return f"김서방은 {i}에 있다"
        
def solution(seoul):
    return f"김서방은 {seoul.index('Kim')}에 있다"