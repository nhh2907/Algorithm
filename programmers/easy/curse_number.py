# https://school.programmers.co.kr/learn/courses/30/lessons/120871
def solution(n):
    # 3의 배수는 1 더하기
    # 3이 나오면 1 더하기
    num = 0
    for i in range(n):
        num += 1
        while (num % 3 == 0) or ("3" in str(num)):
            num += 1

    return num
