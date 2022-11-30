# https://school.programmers.co.kr/learn/courses/30/lessons/120884
def solution(chicken):
    service_num = 0
    while chicken >= 10:
        quotient = chicken // 10
        remainder = chicken % 10
        
        service_num += quotient
        chicken = quotient + remainder
    return service_num


# recursive function
def solution(chicken):
    if chicken < 10:
        return 0
    return chicken//10 + solution(chicken//10 + chicken%10)


# best
def solution(chicken):
    answer = (max(chicken,1)-1)//9
    return answer
