# https://school.programmers.co.kr/learn/courses/30/lessons/136798
def solution(number, limit, power):
    number_list = [i for i in range(1, number+1)]
    answer = 0
    count = 0
    for num in number_list:
        count = 0
        sq_num = int(num**(0.5))
        for i in range(1, sq_num+1):  # 약수 개수 구하기
            if num%i == 0 :
                count += 2
        if num == sq_num**2:
            count -= 1
        if count > limit:  # 공격력 제한 검사
            count = power
        answer += count
    return answer

# best
def solution(number, limit, power):
    iron = 0
    for idx in range(1, number+1):
        knight = [n for n in range(1, int(idx**(0.5)+1)) if not idx%n] # 약수 추출
        knight_power = len(knight) * 2
        if idx == knight[-1]**2:  # 제곱수이면 1개 빼기
            knight_power -= 1
        if knight_power > limit:   # 공격력 제한 검사
            iron += power
        else:
            iron += knight_power
    return iron