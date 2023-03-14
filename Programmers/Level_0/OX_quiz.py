# https://school.programmers.co.kr/learn/courses/30/lessons/120907
def solution(quiz):
    answer = []
    for q in quiz:
        p = q.replace(' - ', ' -').replace(' + ', ' ').replace(' = ', ' ').replace('--', '+')
        nums = list(map(int, p.split()))
        right = nums.pop(-1)
        left = sum(nums)
        if right == left:
            answer.append('O')
        else:
            answer.append('X')

    return answer
