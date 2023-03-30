# https://school.programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    three = ''
    while n > 2:
        remain = n%3
        n = n//3
        three += str(remain)
    three += str(n)
    three = three[::-1]
    
    m = len(three)
    answer = 0
    for i in range(m):
        answer += int(three[i]) * 3**i
    
    return answer


# best
def solution(n):
    three = ''
    while n:
        remainder = n%3
        n = n//3
        three += str(remainder)
    return int(three, 3)