# https://school.programmers.co.kr/learn/courses/30/lessons/12901
def solution(a, b):
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month = [31, 29, 31, 30, 31,30, 31, 31, 30, 31, 30, 31]
    
    days = sum(month[:a-1])+b
    return week[(days%7)]
