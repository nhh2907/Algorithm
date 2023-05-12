# https://school.programmers.co.kr/learn/courses/30/lessons/12940?language=python3
def solution(n, m):
    answer = []
    for i in range(n, 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    return answer+[n*m//answer[0]]

def solution(n, m):
    gcd = lambda a, b: b if not a%b else gcd(b, a%b)
    lcm = (n*m)
    return [gcd(n,m), lcm/gcd(n,m)]