# https://school.programmers.co.kr/learn/courses/30/lessons/77884
def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        count = 0
        for i in range(1, int(num**(0.5))+1):
            if not num%i:
                count += 2
        if num == i**2:
            count -= 1
        if count%2 == 0:
            answer += num
        else:
            answer -= num
    return answer

# best
def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if num**(0.5) == int(num**(0.5)):     # 약수의 개수가 홀수인 수는 제곱수
            answer -= num
        else:
            answer += num
    return answer