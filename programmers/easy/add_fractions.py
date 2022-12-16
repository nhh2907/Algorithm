# https://school.programmers.co.kr/learn/courses/30/lessons/120808
def solution(denum1, num1, denum2, num2):

    # 분모
    num_total = num1 * num2
    a = num_total // num1
    b = num_total // num2

    # 분자
    denum1a = denum1 * a
    denum2b = denum2 * b
    denum_total = denum1a + denum2b
    
    # 약수 찾기
	lis = []
    for i in range(1, min(num_total, denum_total)+1):
        if (denum_total % i == 0) and (num_total % i == 0):
            lis.append(i)
    
    answer = [denum_total//lis[-1], num_total/lis[-1]] # 최대공약수로 나누기
    return answer

# best
def solution(denum1, num1, denum2, num2):
    answer = [denum1 * num2 + denum2 * num1, num1 * num2]

    for i in range(min(answer), 1 , -1):
        if answer[0] % i == 0 and answer[1] % i == 0:
            return [answer[0]//i , answer[1]//i]
    return answer
