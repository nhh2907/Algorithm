# https://school.programmers.co.kr/learn/courses/30/lessons/120842
def solution(num_list, n):
    answer = []
    while len(num_list) != 0:
        temp = []
        for _ in range(n):
            temp.append(num_list.pop(0))
        answer.append(temp)
    return answer

# best
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer