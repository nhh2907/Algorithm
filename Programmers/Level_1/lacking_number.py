# https://school.programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    answer = money - price*sum(range(1, count+1))
    if answer > 0:
        answer = 0
    return abs(answer)

def solution(price, money, count):
    return max(0, price*(1+count)*count//2-money) # 등차수열의 합 공식을 이용